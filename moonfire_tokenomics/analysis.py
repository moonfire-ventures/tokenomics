import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

from moonfire_tokenomics.make_dataset import tokens_to_df
from moonfire_tokenomics.tokens import Tokens

rename_dict = {
    "advisors": "Advisors",
    "airdrop": "Airdrop",
    "investors": "Investors",
    "ecosystem incentives": "Ecosystem",
    "public sale": "Public Sale",
    "team": "Team",
    "treasury": "Treasury",
}

if __name__ == "__main__":
    data = [token[1] for token in Tokens.choices()]
    df = tokens_to_df(data)
    df = df.sort_values(["token", "month"]).drop_duplicates(["token", "type"], keep="last")
    df_grouped = df.groupby(["sector", "token", "common_type"])["share"].sum()
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
    plt.show()
