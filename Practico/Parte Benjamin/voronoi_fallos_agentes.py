# -*- coding: utf-8 -*-
"""
Trabajo Práctico - Periodismo de Datos | Visualización de Datos UTFSM 2026
Parte individual: Benjamín Olguín Pozo

Visualización: VORONOI TREEMAP PONDERADO (jerárquico, 2 niveles)
  - Nivel externo : tipo de fallo de agentes LLM   (área  ∝ frecuencia)
  - Nivel interno : dominio de la tarea            (área  ∝ frecuencia tipo×dominio)
  - Color         : severidad media de la celda    (Low=1 … Critical=4)

Fuente: benchmark_1500.csv (Kaggle - LLM Agent Failure Analysis Benchmark, sintético).

No existe librería mantenida en Python para el Voronoi treemap ponderado, por lo que
el algoritmo (diagrama de potencia + relajación de Lloyd con ajuste de pesos para que
el ÁREA de cada celda sea proporcional a su valor) se implementa a mano más abajo.
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib import cm, colors as mcolors
import matplotlib.patheffects as pe
from shapely.geometry import Polygon, Point

rng = np.random.default_rng(42)

# --------------------------------------------------------------------------- #
#  1. ALGORITMO: VORONOI TREEMAP PONDERADO (power diagram + Lloyd)
# --------------------------------------------------------------------------- #

def _clip_halfplane(poly: Polygon, a: np.ndarray, b: float) -> Polygon:
    """Intersecta `poly` con el semiplano  a·x <= b  (lado interior)."""
    norm = np.linalg.norm(a)
    if norm < 1e-12:
        return poly
    a_hat = a / norm
    b_n = b / norm
    x0 = a_hat * b_n                     # punto sobre la recta a·x = b
    t = np.array([-a_hat[1], a_hat[0]])  # dirección tangente a la recta
    L = 1e5
    p1 = x0 + t * L
    p2 = x0 - t * L
    p3 = p2 - a_hat * L                  # se extiende hacia el lado interior (-a_hat)
    p4 = p1 - a_hat * L
    half = Polygon([p1, p2, p3, p4])
    res = poly.intersection(half)
    if res.is_empty or res.geom_type != "Polygon":
        # ante geometrías degeneradas devolvemos un polígono vacío manejable
        return Polygon()
    return res


def power_cells(sites, weights, clip):
    """Celdas del diagrama de potencia de `sites` (con pesos) recortadas a `clip`."""
    cells = []
    n = len(sites)
    s2 = (sites ** 2).sum(axis=1)        # |s_i|^2
    for i in range(n):
        cell = clip
        for j in range(n):
            if i == j:
                continue
            a = 2.0 * (sites[j] - sites[i])
            b = (s2[j] - weights[j]) - (s2[i] - weights[i])
            cell = _clip_halfplane(cell, a, b)
            if cell.is_empty:
                break
        cells.append(cell)
    return cells


def weighted_voronoi_treemap(targets, clip, iters=140, seed=0):
    """
    Devuelve una lista de polígonos shapely cuyas ÁREAS son proporcionales a
    `targets`, teselando completamente el polígono `clip`.
    """
    local_rng = np.random.default_rng(seed)
    targets = np.asarray(targets, dtype=float)
    targets = targets / targets.sum()
    total_area = clip.area
    n = len(targets)

    # --- sitios iniciales: muestreo por rechazo dentro de clip ---
    minx, miny, maxx, maxy = clip.bounds
    sites = []
    while len(sites) < n:
        p = np.array([local_rng.uniform(minx, maxx),
                      local_rng.uniform(miny, maxy)])
        if clip.contains(Point(p)):
            sites.append(p)
    sites = np.array(sites)

    diag = np.hypot(maxx - minx, maxy - miny)
    weights = np.full(n, (diag * 0.05) ** 2)

    for _ in range(iters):
        cells = power_cells(sites, weights, clip)

        # reparar celdas vacías reubicando el sitio dentro de clip
        for i, c in enumerate(cells):
            if c.is_empty or c.area <= 0:
                while True:
                    p = np.array([local_rng.uniform(minx, maxx),
                                  local_rng.uniform(miny, maxy)])
                    if clip.contains(Point(p)):
                        sites[i] = p
                        weights[i] *= 0.5
                        break
        cells = power_cells(sites, weights, clip)

        areas = np.array([c.area if not c.is_empty else 1e-9 for c in cells])

        # --- ajuste de pesos (regla de razón de áreas, d3-weighted-voronoi) ---
        target_area = targets * total_area
        adapt = np.sqrt(target_area / areas)
        weights = weights * adapt

        # clamp: el radio equivalente no debe superar la distancia al vecino más cercano
        for i in range(n):
            d = np.min([np.hypot(*(sites[i] - sites[j])) for j in range(n) if j != i])
            weights[i] = min(weights[i], (0.95 * d) ** 2)
            weights[i] = max(weights[i], 1e-9)

        # --- relajación de Lloyd: mover sitio al centroide de su celda ---
        new_sites = sites.copy()
        for i, c in enumerate(cells):
            if not c.is_empty and c.area > 0:
                cx, cy = c.centroid.x, c.centroid.y
                new_sites[i] = sites[i] + 0.9 * (np.array([cx, cy]) - sites[i])
        sites = new_sites

    return power_cells(sites, weights, clip)


# --------------------------------------------------------------------------- #
#  2. DATOS
# --------------------------------------------------------------------------- #

df = pd.read_csv("benchmark_1500.csv")
SEV = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
df["sev"] = df["failure_severity"].map(SEV)

# orden de tipos de fallo por frecuencia (mayor a menor)
type_order = df["failure_type"].value_counts().index.tolist()
type_freq = df["failure_type"].value_counts()

DOM_ABBR = {
    "Coding": "Cod", "Mathematics": "Mat", "RAG/QA": "RAG",
    "Planning": "Plan", "Customer Support": "CS",
}

# --------------------------------------------------------------------------- #
#  3. NIVEL EXTERNO: tipos de fallo dentro de un círculo
# --------------------------------------------------------------------------- #

R = 100.0
clip_circle = Point(0, 0).buffer(R, resolution=128)

outer_targets = [type_freq[t] for t in type_order]
print("Calculando nivel externo (12 tipos de fallo)...")
outer_cells = weighted_voronoi_treemap(outer_targets, clip_circle, iters=160, seed=7)

# --------------------------------------------------------------------------- #
#  4. NIVEL INTERNO: dominios dentro de cada tipo de fallo
# --------------------------------------------------------------------------- #

cmap = matplotlib.colormaps["YlOrRd"]
norm = mcolors.Normalize(vmin=1.0, vmax=4.0)

# severidad media por tipo de fallo (para la leyenda)
type_sev = df.groupby("failure_type")["sev"].mean()

# --- lienzo: gráfico a la izquierda + panel de leyenda a la derecha ---
fig = plt.figure(figsize=(17, 13))
grid = fig.add_gridspec(1, 2, width_ratios=[13, 4.6], wspace=0.02)
ax = fig.add_subplot(grid[0])
lax = fig.add_subplot(grid[1])
ax.set_aspect("equal")
ax.axis("off")
lax.axis("off")

clip_area = clip_circle.area
badges = []  # (numero, x, y) — se dibujan al final, encima de todo

for idx, (t, ocell) in enumerate(zip(type_order, outer_cells), start=1):
    if ocell.is_empty or ocell.area <= 0:
        continue
    sub = df[df["failure_type"] == t]
    dom_counts = sub.groupby("domain").size()
    dom_counts = dom_counts[dom_counts > 0]
    doms = dom_counts.index.tolist()

    print(f"  - {idx}. {t}: {len(doms)} dominios")
    if len(doms) == 1:
        inner_cells = [ocell]
    else:
        inner_cells = weighted_voronoi_treemap(
            dom_counts.values, ocell, iters=120, seed=hash(t) % 9999
        )

    for dom, icell in zip(doms, inner_cells):
        if icell.is_empty or icell.area <= 0:
            continue
        sev_mean = sub[sub["domain"] == dom]["sev"].mean()
        color = cmap(norm(sev_mean))
        xs, ys = icell.exterior.xy
        ax.add_patch(MplPolygon(np.column_stack([xs, ys]), closed=True,
                                facecolor=color, edgecolor="white", linewidth=1.2))
        # etiqueta del dominio con fuente proporcional al tamaño de la celda
        frac = icell.area / clip_area
        if frac > 0.004:
            fs = float(np.clip(np.sqrt(frac) * 95, 5.0, 11.0))
            cx, cy = icell.centroid.x, icell.centroid.y
            txt_col = "white" if sev_mean > 2.7 else "#333333"
            halo = "#333333" if sev_mean > 2.7 else "white"
            ax.text(cx, cy, DOM_ABBR.get(dom, dom), ha="center", va="center",
                    fontsize=fs, color=txt_col, fontweight="bold", zorder=4,
                    path_effects=[pe.withStroke(linewidth=1.6, foreground=halo)])

    # borde grueso del tipo de fallo
    oxs, oys = ocell.exterior.xy
    ax.add_patch(MplPolygon(np.column_stack([oxs, oys]), closed=True,
                            facecolor="none", edgecolor="black", linewidth=2.6))
    badges.append((idx, ocell.centroid.x, ocell.centroid.y))

# --- badges numéricos (encima de todo) ---
badge_r = R * 0.052
for num, bx, by in badges:
    ax.add_patch(plt.Circle((bx, by), badge_r, facecolor="white",
                            edgecolor="black", linewidth=1.4, zorder=6))
    ax.text(bx, by, str(num), ha="center", va="center", fontsize=11,
            fontweight="bold", color="black", zorder=7)

# --------------------------------------------------------------------------- #
#  5. TÍTULO, LEYENDA Y ANOTACIONES
# --------------------------------------------------------------------------- #

ax.set_xlim(-R * 1.06, R * 1.06)
ax.set_ylim(-R * 1.14, R * 1.10)

fig.suptitle("Anatomía de los fallos de agentes LLM: lo que más falla no es lo más peligroso",
             fontsize=18, fontweight="bold", x=0.5, y=0.96)
ax.set_title("Voronoi treemap — área ∝ frecuencia del tipo de fallo · color ∝ severidad media "
             "· subdivisión interna por dominio",
             fontsize=11, color="#444444", pad=12)

# --- panel de leyenda numerada (derecha) ---
lax.set_xlim(0, 1)
lax.set_ylim(0, 1)
lax.text(0.0, 0.985, "Tipos de fallo  (N° = ranking de frecuencia)",
         fontsize=12, fontweight="bold", va="top")
n_items = len(type_order)
y0, y1 = 0.93, 0.10
for i, t in enumerate(type_order):
    y = y0 + (y1 - y0) * (i / (n_items - 1))
    sev = type_sev[t]
    # micro-swatch de color = severidad media del tipo
    lax.add_patch(plt.Rectangle((0.02, y - 0.018), 0.05, 0.036,
                                facecolor=cmap(norm(sev)), edgecolor="#888888",
                                linewidth=0.6, transform=lax.transAxes))
    lax.text(0.10, y, f"{i+1}.  {t.replace(' Failure', '')}",
             fontsize=11, va="center", fontweight="bold")
    lax.text(0.10, y - 0.028, f"n = {type_freq[t]}   ·   sev media {sev:.1f}",
             fontsize=9, va="center", color="#555555")

sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation="horizontal", fraction=0.045, pad=0.03,
                    ticks=[1, 2, 3, 4])
cbar.ax.set_xticklabels(["Low (1)", "Medium (2)", "High (3)", "Critical (4)"])
cbar.set_label("Severidad media de la celda", fontsize=10)

fig.text(0.5, 0.045,
         "Dominios:  Cod=Coding · Mat=Mathematics · RAG=RAG/QA · Plan=Planning · CS=Customer Support     "
         "|     Fuente: Kaggle — LLM Agent Failure Analysis Benchmark (1.500 casos, dataset sintético)",
         ha="center", va="center", fontsize=8.5, color="#666666")

plt.savefig("voronoi_fallos_agentes.png", dpi=150, bbox_inches="tight", facecolor="white")
print("\nGuardado: voronoi_fallos_agentes.png")
