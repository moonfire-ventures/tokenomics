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
    allocations: List[Allocation]
    sources: List[str]
    year: Optional[int] = None
