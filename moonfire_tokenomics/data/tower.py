from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

tower = Token(
    token="TOWER",
    project="Crazy Defense Heroes",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Play to Earn", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="Marketing Fund Pool", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Liquidity Pool", common_type=CommonType.TREASURY, share=0.15),
                AllocationRecord(type="Team and Advisors", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Company Reserve Pool", common_type=CommonType.TREASURY, share=0.15),
                AllocationRecord(type="Community Development", common_type=CommonType.ECOSYSTEM, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://wiki.rugdoc.io/docs/introduction-to-crazy-defense-heroes/",
    ],
)
