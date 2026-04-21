import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "train.csv"

# Cantidad de modelos más presentes a mostrar
TOP_N = 8

# Leer dataset
df = pd.read_csv(DATASET_PATH)

# Nos quedamos solo con batallas decididas (sin empate)
dec = df[(df["winner_model_a"] == 1) | (df["winner_model_b"] == 1)].copy()

# Crear columnas winner y loser
dec["winner"] = np.where(dec["winner_model_a"] == 1, dec["model_a"], dec["model_b"])
dec["loser"]  = np.where(dec["winner_model_a"] == 1, dec["model_b"], dec["model_a"])

# Encontrar los modelos con más apariciones
appearances = pd.concat([df["model_a"], df["model_b"]], ignore_index=True).value_counts()
top_models = appearances.head(TOP_N).index.tolist()

# Resumen por modelo
summary = []

for model in top_models:
    wins = int((dec["winner"] == model).sum())
    losses = int((dec["loser"] == model).sum())
    ties = int(((df["winner_tie"] == 1) & ((df["model_a"] == model) | (df["model_b"] == model))).sum())
    decisive = wins + losses

    summary.append({
        "model": model,
        "appearances": int(appearances[model]),
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "decisive_battles": decisive,
        "win_rate_decisive": round(wins / decisive, 4) if decisive > 0 else None
    })

summary_df = pd.DataFrame(summary).sort_values("win_rate_decisive", ascending=False)
print("\n=== Resumen de modelos top ===")
print(summary_df)

# Guardar resumen si quieres
summary_df.to_csv("resumen_top_modelos.csv", index=False)

# Construir aristas para Sankey: winner -> loser
edges = (
    dec[dec["winner"].isin(top_models) & dec["loser"].isin(top_models)]
    .groupby(["winner", "loser"], as_index=False)
    .size()
    .rename(columns={"size": "wins"})
    .sort_values("wins", ascending=False)
)

print("\n=== Primeras aristas del Sankey ===")
print(edges.head(15))

# Guardar aristas si quieres
edges.to_csv("sankey_edges_top_modelos.csv", index=False)

# Crear nodos duplicados:
# izquierda = modelos ganadores
# derecha   = modelos perdedores
left_labels = [f"Ganó: {m}" for m in top_models]
right_labels = [f"Perdió: {m}" for m in top_models]
labels = left_labels + right_labels

left_index = {m: i for i, m in enumerate(top_models)}
right_index = {m: i + len(top_models) for i, m in enumerate(top_models)}

sources = edges["winner"].map(left_index).tolist()
targets = edges["loser"].map(right_index).tolist()
values = edges["wins"].tolist()

# Paleta simple
palette = [
    "#4C78A8", "#F58518", "#E45756", "#72B7B2",
    "#54A24B", "#EECA3B", "#B279A2", "#FF9DA6"
]

node_colors = palette[:len(top_models)] + palette[:len(top_models)]
link_colors = [palette[top_models.index(w)] for w in edges["winner"]]

# Crear Sankey
fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    node=dict(
        pad=15,
        thickness=18,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors,
        customdata=[
            f"{winner} derrotó a {loser}: {wins} veces"
            for winner, loser, wins in edges[["winner", "loser", "wins"]].itertuples(index=False)
        ],
        hovertemplate="%{customdata}<extra></extra>"
    )
)])

fig.update_layout(
    title="Sankey de victorias entre los 8 modelos con más presencia en Chatbot Arena 55K",
    font=dict(size=12),
    width=1200,
    height=800
)

# Mostrar en pantalla
fig.show()

# Guardar versión HTML
fig.write_html("sankey_victorias_top8.html", include_plotlyjs="cdn")

print("\nArchivos generados:")
print("- resumen_top_modelos.csv")
print("- sankey_edges_top_modelos.csv")
print("- sankey_victorias_top8.html")