from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

slnd = Token(
    token="SLEND",
    project="Solend",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=36,
            records=[
                AllocationRecord(type="Seed", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Future strategic rounds", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.25),
                AllocationRecord(type="Treasury", common_type=CommonType.TREASURY, share=0.25),
                AllocationRecord(type="IDO", common_type=CommonType.PUBLIC_SALE, share=0.05),
                AllocationRecord(type="Liquidity Mining", common_type=CommonType.ECOSYSTEM, share=0.3),
            ],
        ),
    ],
    sources=[
        "https://docs.solend.fi/protocol/token",
    ],
    year=2021,
)
