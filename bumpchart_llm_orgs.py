import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Epoch Database - Notable Models.csv")
df["Publication date"] = pd.to_datetime(df["Publication date"], errors="coerce")
df = df.dropna(subset=["Publication date", "Organization", "Domain"]).copy()
df["Year"] = df["Publication date"].dt.year

df = df[(df["Year"] >= 2018) & (df["Year"] <= 2025)].copy()
df = df[df["Domain"].str.contains("Language", case=False, na=False)].copy()

def normalize_org(org: str) -> str:
    o = str(org).strip().lower()
    if "google" in o or "deepmind" in o:
        return "Google"
    if "openai" in o:
        return "OpenAI"
    if "anthropic" in o:
        return "Anthropic"
    if "meta" in o:
        return "Meta"
    if "microsoft" in o:
        return "Microsoft"
    if "alibaba" in o:
        return "Alibaba"
    if "nvidia" in o:
        return "NVIDIA"
    if "baidu" in o:
        return "Baidu"
    return "Otros"

df["Org_group"] = df["Organization"].apply(normalize_org)
counts = (
    df.groupby(["Year", "Org_group"])
      .size()
      .reset_index(name="count")
)

top_orgs = (
    counts.groupby("Org_group")["count"]
    .sum()
    .sort_values(ascending=False)
)
top_orgs = [o for o in top_orgs.index.tolist() if o != "Otros"][:7]

years = list(range(2018, 2026))
grid = pd.MultiIndex.from_product([years, top_orgs], names=["Year", "Org_group"]).to_frame(index=False)
counts = grid.merge(counts[counts["Org_group"].isin(top_orgs)], on=["Year", "Org_group"], how="left").fillna({"count": 0})

counts["rank"] = counts.groupby("Year")["count"].rank(method="min", ascending=False)
counts["rank"] = counts["rank"].astype(int)

pivot_rank = counts.pivot(index="Year", columns="Org_group", values="rank").sort_index()
pivot_count = counts.pivot(index="Year", columns="Org_group", values="count").sort_index()

fig, ax = plt.subplots(figsize=(12, 7))

for org in pivot_rank.columns:
    ax.plot(pivot_rank.index, pivot_rank[org], marker="o", linewidth=2, label=org)
    ax.text(
        pivot_rank.index.max() + 0.08,
        pivot_rank.loc[pivot_rank.index.max(), org],
        f"{org} ({int(pivot_count.loc[pivot_count.index.max(), org])})",
        va="center",
        fontsize=9
    )

ax.set_title("Ranking anual de organizaciones por cantidad de modelos LLM notables")
ax.set_xlabel("Año")
ax.set_ylabel("Posición en el ranking")
ax.set_xticks(years)
ax.set_yticks(range(1, len(top_orgs) + 1))
ax.invert_yaxis()
ax.grid(True, alpha=0.3)
ax.set_xlim(min(years), max(years) + 1.1)

if ax.get_legend():
    ax.get_legend().remove()

plt.tight_layout()
plt.savefig("bumpchart_llm_orgs.png", dpi=200, bbox_inches="tight")
plt.show()
