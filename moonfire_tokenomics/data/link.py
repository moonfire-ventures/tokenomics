from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

link = Token(
    token="LINK",
    project="Chainlink",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Public Token Sale", common_type=CommonType.PUBLIC_SALE, share=0.35),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.3),
            ],
        ),
        Allocation(
            month=30,
            records=[
                AllocationRecord(type="Public Token Sale", common_type=CommonType.PUBLIC_SALE, share=0.35),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.3),
                AllocationRecord(type="Node Operators & Ecosystem", common_type=CommonType.ECOSYSTEM, share=0.35),
            ],
        ),
    ],
    sources=[
        "https://messari.io/asset/chainlink/profile/supply-schedule",
    ],
)