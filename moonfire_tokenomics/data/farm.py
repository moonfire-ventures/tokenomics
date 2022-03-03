from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

farm = Token(
    token="FARM",
    project="Harvest Finance",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Liquidity Providers", common_type=CommonType.ECOSYSTEM, share=0.7),
                AllocationRecord(type="Operational Treasury", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Development Team", common_type=CommonType.TEAM, share=0.2),
            ],
        ),
    ],
    sources=[
        "https://harvest-finance.gitbook.io/harvest-finance/general-info/what-do-we-do/profit-share-pool-and-farm-tokenomics",  # noqa
    ],
    year=2020,
)
