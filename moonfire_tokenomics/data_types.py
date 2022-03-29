from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from dataclasses_json import DataClassJsonMixin


class Sector(str, Enum):
    DEFI = "defi"
    GAMING = "gaming"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Blockchain(str, Enum):
    ETH = "Ethereum"
    SOL = "Solana"
    BSC = "Binance Smart Chain"
    POLY = "Polygon"
    TERRA = "Terra"
    AVAX = "Avalanche"
    X = "Immutable X"
    ONE = "Harmony"
    RONIN = "Ronin"
    GC = "Gnosis"
    FTM = "Fantom"
    SORA = "Sora"
    TOMO = "Tomochain"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Category(str, Enum):
    GOV = "Governance"
    DIVIDEND = "Dividend"
    PAYMENT = "Payment"
    ACCESS = "Access"
    OTHER = "Other"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class CommonType(str, Enum):
    AIRDROP = "airdrop"
    ECOSYSTEM = "ecosystem incentives"
    TREASURY = "treasury"
    TEAM = "team"
    INVESTORS = "investors"
    ADVISORS = "advisors"
    PUBLIC_SALE = "public sale"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


@dataclass
class AllocationRecord(DataClassJsonMixin):
    type: str
    common_type: str
    share: float


@dataclass
class Allocation(DataClassJsonMixin):
    month: int
    records: List[AllocationRecord]


@dataclass
class Token(DataClassJsonMixin):
    name: str
    project: str
    sector: Sector
    blockchain: List[Blockchain]
    category: List[Category]
    capped: bool
    allocations: List[Allocation]
    sources: List[str]
    year: Optional[int] = None
