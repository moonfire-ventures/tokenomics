from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

sand = Token(
    token="SAND",
    project="Sandbox",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Binance Launchpad Sale", common_type=CommonType.PUBLIC_SALE, share=0.12),
                AllocationRecord(type="Foundation", common_type=CommonType.ECOSYSTEM, share=0.0583),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.002),
                AllocationRecord(type="Company Reserve", common_type=CommonType.TREASURY, share=0.0547),
            ],
        ),
        Allocation(
            month=54,
            records=[
                AllocationRecord(type="Binance Launchpad Sale", common_type=CommonType.PUBLIC_SALE, share=0.12),
                AllocationRecord(type="Seed Sale", common_type=CommonType.INVESTORS, share=0.1718),
                AllocationRecord(type="Strategic Sale", common_type=CommonType.INVESTORS, share=0.04),
                AllocationRecord(type="Foundation", common_type=CommonType.ECOSYSTEM, share=0.12),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.19),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.1),
                AllocationRecord(type="Company Reserve", common_type=CommonType.TREASURY, share=0.2582),
            ],
        ),
    ],
    sources=[
        "https://research.binance.com/en/projects/the-sandbox",
        "https://cryptobulls.info/what-is-the-sandbox-metaverse-nft-game#What_is_the_Metaverse_SAND_revenue_model",
    ],
    year=2020,
)
