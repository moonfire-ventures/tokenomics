from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

lrc = Token(
    token="LRC",
    project="Loopring",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Investors", common_type=CommonType.PUBLIC_SALE, share=0.5),
                AllocationRecord(
                    type="Loopring Ecosystem Advancement Fund", common_type=CommonType.ECOSYSTEM, share=0.2
                ),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Contractors, Auditor, Exchanges", common_type=CommonType.TREASURY, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://coin98insights.com/loopring-lrc",
    ],
)
