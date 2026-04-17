import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

df = pd.read_csv("Epoch Database - Notable Models.csv")

df["Publication date"] = pd.to_datetime(df["Publication date"], errors="coerce")
df = df.dropna(subset=["Publication date", "Organization", "Domain"]).copy()
df = df[df["Domain"].str.contains("Language", case=False, na=False)].copy()

df["Year"] = df["Publication date"].dt.year
df = df[(df["Year"] >= 2018) & (df["Year"] <= 2026)].copy()
def normalize_org(org):
    org = str(org).strip().lower()
    if "google" in org or "deepmind" in org:
        return "Google"
    elif "openai" in org:
        return "OpenAI"
    elif "anthropic" in org:
        return "Anthropic"
    elif "meta" in org:
        return "Meta"
    elif "microsoft" in org:
        return "Microsoft"
    elif "alibaba" in org:
        return "Alibaba"
    elif "nvidia" in org:
        return "NVIDIA"
    elif "baidu" in org:
        return "Baidu"
    else:
        return "Otros"

df["Org_group"] = df["Organization"].apply(normalize_org)
df = df[df["Org_group"] != "Otros"].copy()

pivot = (
    df.pivot_table(
        index="Year",
        columns="Org_group",
        values="Model",
        aggfunc="count",
        fill_value=0
    )
    .sort_index()
)

pivot = pivot[pivot.sum().sort_values(ascending=False).index]

x = pivot.index.to_numpy()
x_smooth = np.linspace(x.min(), x.max(), 300)

smooth_series = []
for col in pivot.columns:
    y = pivot[col].to_numpy()
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_smooth)
    y_smooth = np.clip(y_smooth, 0, None)
    smooth_series.append(y_smooth)

plt.figure(figsize=(14, 7))
plt.stackplot(
    x_smooth,
    smooth_series,
    labels=pivot.columns,
    baseline="wiggle"
)

plt.title("Evolución temporal de modelos de lenguaje notables por organización")
plt.xlabel("Año de publicación")
plt.ylabel("Cantidad de modelos")
plt.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0))
plt.tight_layout()
plt.savefig("Grafico1.png", dpi=300, bbox_inches="tight")
print("Gráfico guardado como Grafico1.png")