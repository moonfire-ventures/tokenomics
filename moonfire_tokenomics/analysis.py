import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

from moonfire_tokenomics.make_dataset import tokens_to_df
from moonfire_tokenomics.tokens import Tokens

matplotlib.rc("figure", dpi=192)

rename_dict = {
    "advisors": "Advisors",
    "airdrop": "Airdrop",
    "investors": "Investors",
    "ecosystem incentives": "Ecosystem",
    "public sale": "Public Sale",
    "team": "Team",
    "treasury": "Treasury",
}

blockchain_colour_map = {
    "Ethereum": "navy",
    "Solana": "teal",
    "Binance Smart Chain": "gold",
    "Polygon": "blueviolet",
    "Terra": "blue",
    "Avalanche": "orangered",
    "Immutable X": "darkturquoise",
    "Harmony": "skyblue",
    "Ronin": "dodgerblue",
    "Gnosis": "seagreen",
    "Fantom": "cornflowerblue",
    "Sora": "red",
    "Tomochain": "mediumspringgreen",
}

category_colour_map = {
    "Governance": "navy",
    "Payment": "darkorange",
    "Dividend": "slategrey",
    "Access": "gold",
    "Other": "cadetblue",
}

if __name__ == "__main__":
    data = [token[1] for token in Tokens.choices()]
    df = tokens_to_df(data)
    sns.set_theme(style="whitegrid")
    # fmt: off
    chain_df = (
        df
        .explode("blockchain")
        .drop_duplicates(subset=["name", "blockchain"])
        .groupby(["blockchain", "sector"])["share"].count()
        .sort_values(ascending=False)
        .unstack(0)
        .fillna(0)
        .assign(total=lambda d: d.sum(1))
        .sort_values(by="total", ascending=False)
    )
    chain_df.loc["Total"] = chain_df.sum(axis=0)
    chain_df = (
        chain_df
        .div(chain_df["total"], axis=0)
        .drop(columns=["total"])
        .T.sort_values("Total", ascending=False).T
        .rename(index={"defi": "DeFi", "gaming": "Gaming"})
        .sort_index(ascending=False)
    )
    ax = chain_df.plot.barh(stacked=True, color=blockchain_colour_map, figsize=(10, 5))
    ax.xaxis.set_major_formatter(PercentFormatter(1))
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_ylabel("")
    plt.title("Blockchain support by sector")
    plt.tight_layout()
    plt.show()

    category_df = (
        df
        .explode("category")
        .drop_duplicates(subset=["name", "category"])
        .groupby(["category", "sector"])["share"].count()
        .unstack(0)
        .fillna(0)
        .assign(total=lambda d: d.sum(1))
        .sort_values(by="total", ascending=False)
    )
    category_df.loc["Total"] = category_df.sum(axis=0)
    category_df = (
        category_df
        .div(category_df["total"], axis=0)
        .drop(columns=["total"])
        .T.sort_values("Total", ascending=False).T
        .rename(index={"defi": "DeFi", "gaming": "Gaming"})
        .sort_index(ascending=False)
    )
    sns.set_color_codes("bright")
    ax = category_df.plot.barh(stacked=True, color=category_colour_map, figsize=(10, 5))
    ax.xaxis.set_major_formatter(PercentFormatter(1))
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_ylabel("")
    plt.title("Token usages by sector")
    plt.tight_layout()
    plt.show()

    capped_df = (
        df
        .drop_duplicates(subset=["name", "capped"])
        .groupby(["capped", "sector"])["share"].count()
        .unstack(0)
        .assign(total=lambda d: d.sum(1))
        .sort_values(by="total", ascending=False)
    )
    capped_df.loc["Total"] = capped_df.sum(axis=0)
    capped_df = (
        capped_df
        .div(capped_df["total"], axis=0)
        .drop(columns=["total"])
        .T.sort_values("Total", ascending=False).T
        .rename(index={"defi": "DeFi", "gaming": "Gaming"})
        .sort_index(ascending=False)
    )
    ax = capped_df.plot.barh(stacked=True, color=["navy", "darkorange"], figsize=(10, 5))
    ax.xaxis.set_major_formatter(PercentFormatter(1))
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_ylabel("")
    plt.title("Share of projects with capped token supply by sector")
    plt.tight_layout()
    plt.show()
    # fmt: on

    df = df.sort_values(["name", "month"]).drop_duplicates(["name", "type"], keep="last")
    df_yearly = df.drop_duplicates(["year", "name"]).groupby(["year", "sector"])["share"].count().unstack().fillna(0)
    df_yearly.plot.bar(stacked=True, color=["m", "g"])
    plt.title("Number of projects by sector over time")
    plt.tight_layout()
    plt.show()

    df_grouped = df.groupby(["sector", "name", "common_type"])["share"].sum()
    df_grouped.unstack().groupby(["sector"]).describe()

    display_df = df_grouped.unstack().fillna(0).stack().reset_index()
    display_df["common_type"] = display_df["common_type"].apply(lambda x: rename_dict[str(x)])
    fig, axs = plt.subplots(figsize=(12, 7))
    ax = plt.gca()
    sns.stripplot(
        data=display_df, y=0, x="common_type", hue="sector", dodge=True, zorder=1, orient="v", ax=ax, palette=["m", "g"]
    )
    sns.boxplot(
        y=0,
        x="common_type",
        data=display_df,
        fliersize=0,
        width=0.6,
        hue="sector",
        orient="v",
        ax=ax,
        palette=["m", "g"],
        boxprops=dict(alpha=0.2),
    )
    plt.ylabel("Allocation")
    plt.xlabel("")
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    plt.legend(labels=["DeFi", "Gaming"])
    plt.title("Token Allocations of Popular DeFi and Crypto Gaming Applications")
    plt.tight_layout()
    plt.show()
