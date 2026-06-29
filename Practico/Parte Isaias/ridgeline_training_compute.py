import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from pathlib import Path

# ============================================================
# Ridgeline / Joyplot:
# Escala de entrenamiento de modelos LLM notables por año
# Fuente: Epoch AI - Notable Models
# ============================================================

RAW_FILE = "Epoch Database - Notable Models.csv"
OUTPUT_DATASET = "llm_training_compute_ridgeline_dataset.csv"
OUTPUT_FIGURE = "ridgeline_training_compute.png"

YEAR_MIN = 2018
YEAR_MAX = 2025


def classify_open_status(value):
    """Convierte la columna original 'Open model weights?' a etiquetas legibles."""
    if pd.isna(value):
        return "Sin dato"

    text = str(value).strip().lower()

    if text == "yes":
        return "Abierto"
    if text == "no":
        return "Cerrado"

    return "Sin dato"


# =========================
# 1. Cargar dataset
# =========================

raw_path = Path(RAW_FILE)

if not raw_path.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo {RAW_FILE}. "
        "Déjalo en la misma carpeta que este script."
    )

df = pd.read_csv(raw_path)

# =========================
# 2. Limpieza y filtrado
# =========================

df["Publication date"] = pd.to_datetime(df["Publication date"], errors="coerce")
df["Training compute (FLOP)"] = pd.to_numeric(
    df["Training compute (FLOP)"],
    errors="coerce"
)

df = df.dropna(
    subset=[
        "Publication date",
        "Domain",
        "Training compute (FLOP)"
    ]
).copy()

# Filtrar modelos del dominio lenguaje / LLM
df = df[
    df["Domain"].astype(str).str.contains("Language", case=False, na=False)
].copy()

# Año de publicación
df["Year"] = df["Publication date"].dt.year

# Rango usado en las tareas anteriores
df = df[
    (df["Year"] >= YEAR_MIN) &
    (df["Year"] <= YEAR_MAX)
].copy()

# El cómputo de entrenamiento debe ser positivo
df = df[df["Training compute (FLOP)"] > 0].copy()

# Transformación logarítmica para poder visualizar FLOP
df["log10_training_compute"] = np.log10(df["Training compute (FLOP)"])

# Columna auxiliar opcional para futuras visualizaciones
df["Open_Status"] = df["Open model weights?"].apply(classify_open_status)

# Dataset reducido para revisión / informe
columns_to_export = [
    "Model",
    "Organization",
    "Country (of organization)",
    "Publication date",
    "Year",
    "Domain",
    "Training compute (FLOP)",
    "log10_training_compute",
    "Parameters",
    "Training compute cost (2023 USD)",
    "Open model weights?",
    "Open_Status",
    "Model accessibility",
    "Frontier model",
]

dataset = (
    df[columns_to_export]
    .sort_values(["Year", "log10_training_compute", "Model"])
    .reset_index(drop=True)
)

dataset.to_csv(OUTPUT_DATASET, index=False, encoding="utf-8-sig")

print(f"Dataset procesado guardado como: {OUTPUT_DATASET}")
print(f"Registros usados: {len(dataset)}")
print("Registros por año:")
print(dataset.groupby("Year").size())

# =========================
# 3. Crear ridgeline plot
# =========================

years = list(range(YEAR_MIN, YEAR_MAX + 1))

x_min = np.floor(dataset["log10_training_compute"].min()) - 0.25
x_max = np.ceil(dataset["log10_training_compute"].max()) + 0.25
x_grid = np.linspace(x_min, x_max, 600)

fig, ax = plt.subplots(figsize=(12, 8))

vertical_gap = 1.0
max_height = 0.85

for i, year in enumerate(years):
    values = dataset.loc[
        dataset["Year"] == year,
        "log10_training_compute"
    ].dropna().to_numpy()

    if len(values) == 0:
        continue

    y_base = i * vertical_gap

    # Si hay varios modelos, usamos KDE.
    # Si hubiera solo uno, dibujamos una curva normal artificial centrada en el dato.
    if len(values) >= 2:
        kde = gaussian_kde(values)
        density = kde(x_grid)
    else:
        center = values[0]
        density = np.exp(-0.5 * ((x_grid - center) / 0.12) ** 2)

    # Normalizar altura para que todas las "montañas" sean comparables visualmente
    if density.max() > 0:
        density = density / density.max() * max_height

    ax.fill_between(
        x_grid,
        y_base,
        y_base + density,
        alpha=0.75
    )

    ax.plot(
        x_grid,
        y_base + density,
        linewidth=1.2
    )

    # Mediana del año como marca breve
    median_value = np.median(values)
    ax.plot(
        [median_value, median_value],
        [y_base, y_base + max_height * 0.12],
        linewidth=2
    )

    # Etiqueta año + cantidad de modelos
    ax.text(
        x_min - 0.18,
        y_base + 0.04,
        f"{year}  n={len(values)}",
        ha="right",
        va="bottom",
        fontsize=10
    )

# =========================
# 4. Estética del gráfico
# =========================

ax.set_title(
    "Escala de entrenamiento de modelos LLM notables",
    fontsize=16,
    weight="bold",
    pad=16
)

ax.text(
    0,
    1.01,
    "Distribución anual del cómputo de entrenamiento, expresado como log10(FLOP), para modelos de lenguaje publicados entre 2018 y 2025.",
    transform=ax.transAxes,
    fontsize=10,
    va="bottom"
)

ax.set_xlabel("log10(FLOP de entrenamiento)", fontsize=11)
ax.set_yticks([])

ax.set_xlim(x_min - 0.4, x_max)
ax.set_ylim(-0.15, (len(years) - 1) * vertical_gap + 1.05)

ax.grid(axis="x", alpha=0.25)

for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

ax.text(
    0,
    -0.10,
    "Fuente: Epoch AI – Notable Models. Elaboración propia. "
    "Filtro: Domain contiene 'Language', años 2018–2025, registros con Training compute (FLOP) disponible.",
    transform=ax.transAxes,
    fontsize=9,
    va="top"
)

plt.tight_layout()
plt.savefig(OUTPUT_FIGURE, dpi=300, bbox_inches="tight")
plt.show()

print(f"Visualización guardada como: {OUTPUT_FIGURE}")
