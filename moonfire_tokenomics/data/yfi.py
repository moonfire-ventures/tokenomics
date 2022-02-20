from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

yfi = Token(
    token="YFI",
    project="yearn.finance",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Liquidity Providers", common_type=CommonType.ECOSYSTEM, share=1.0),
            ],
        ),
    ],
    sources=[
        "https://www.gemini.com/cryptopedia/what-is-yearn-finance-yfi-coin-yearnfinance#section-what-is-yearn-finance",
    ],
)