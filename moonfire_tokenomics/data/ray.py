from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

ray = Token(
    token="RAY",
    project="Raydium",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=36,
            records=[
                AllocationRecord(type="Mining Reserve", common_type=CommonType.ECOSYSTEM, share=0.34),
                AllocationRecord(type="Partnership & Ecosystem", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Liquidity for AMM at Launch", common_type=CommonType.ECOSYSTEM, share=0.08),
                AllocationRecord(type="Community & Seed funding", common_type=CommonType.PUBLIC_SALE, share=0.06),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.02),
            ],
        ),
    ],
    sources=[
        "https://insights.glassnode.com/uni-token-is-uniswap-really-decentralized/",
        "https://uniswap.org/blog/uni",
    ],
    year=2021,
)
