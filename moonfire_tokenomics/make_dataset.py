import argparse
import os
from typing import List

import pandas as pd

from moonfire_tokenomics.data_types import Token
from moonfire_tokenomics.tokens import Tokens


def tokens_to_df(tokens: List[Token]) -> pd.DataFrame:
    df = pd.DataFrame(tokens).explode("allocations").explode("sources")
    df = pd.concat([df.drop(["allocations", "sources"], axis=1), df["allocations"].apply(pd.Series)], axis=1)
    df = df.explode("records")
    df = pd.concat([df.drop(["records"], axis=1), df["records"].apply(pd.Series)], axis=1)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, help="Directory where to save data set", required=True)
    args = parser.parse_args()
    data = [token[1] for token in Tokens.choices()]
    df = tokens_to_df(data)
    df.to_csv(os.path.join(args.dir, "token_allocations.csv"), index=False)
