from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

bcmc = Token(
    token="BCMC",
    project="Blockchain Monster Hunt",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Public Round", common_type=CommonType.PUBLIC_SALE, share=0.005),
                AllocationRecord(type="Private Investor", common_type=CommonType.INVESTORS, share=0.098),
                AllocationRecord(type="Marketing & Partnership", common_type=CommonType.ECOSYSTEM, share=0.141),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.18),
                AllocationRecord(type="Eco-System", common_type=CommonType.ECOSYSTEM, share=0.176),
                AllocationRecord(type="Mining", common_type=CommonType.ECOSYSTEM, share=0.4),
            ],
        ),
    ],
    sources=[
        "https://bcmhunt.com/howtoplay",
    ],
)
