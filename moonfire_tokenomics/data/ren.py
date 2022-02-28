from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

ren = Token(
    token="REN",
    project="Ren",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=24,
            records=[
                AllocationRecord(type="Main Sale", common_type=CommonType.PUBLIC_SALE, share=0.082),
                AllocationRecord(type="Presale", common_type=CommonType.INVESTORS, share=0.52),
                AllocationRecord(type="Team, Founders and Advisors", common_type=CommonType.TEAM, share=0.298),
                AllocationRecord(type="Community Partners", common_type=CommonType.ECOSYSTEM, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://medium.com/@JamesTodaro/republic-protocol-analysis-and-valuation-7ebef4b3c4f9",
    ],
    year=2017,
)
