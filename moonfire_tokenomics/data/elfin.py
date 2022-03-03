from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

elfin = Token(
    token="ELFIN",
    project="Elfin Kingdom",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Strategic Round", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="Private Round", common_type=CommonType.INVESTORS, share=0.15),
                AllocationRecord(type="Public Round", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Community Incentive", common_type=CommonType.ECOSYSTEM, share=0.1),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Advisor", common_type=CommonType.ADVISORS, share=0.05),
                AllocationRecord(type="Farming Incentives", common_type=CommonType.ECOSYSTEM, share=0.4),
                AllocationRecord(type="Marketing & Eco", common_type=CommonType.ECOSYSTEM, share=0.08),
                AllocationRecord(type="Foundation", common_type=CommonType.ECOSYSTEM, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://medium.com/@elfinkingdom/understanding-elfins-token-metrics-5548d16bf273",
    ],
)
