from enum import Enum
from inspect import getmembers

import moonfire_tokenomics.data as data
from moonfire_tokenomics.data_types import Token


class TokensEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


token_list = [item[1] for item in getmembers(data) if isinstance(item[1], Token)]
Tokens = TokensEnum(value="Tokens", names=[(token.name, token) for token in token_list])  # type: ignore
