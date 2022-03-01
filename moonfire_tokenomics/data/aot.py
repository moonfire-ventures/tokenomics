from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

aot = Token(
    name="AOT",
    project="Age of Tanks",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Reserve", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Seed Fund", common_type=CommonType.INVESTORS, share=0.02),
                AllocationRecord(type="Strategic Fund", common_type=CommonType.INVESTORS, share=0.06),
                AllocationRecord(type="IDO", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.05),
                AllocationRecord(type="Public Sales", common_type=CommonType.PUBLIC_SALE, share=0.1),
                AllocationRecord(type="Initial Liquidity", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Partners & Advisors", common_type=CommonType.ADVISORS, share=0.1),
                AllocationRecord(type="Core Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Gameplay Incentives", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Game Development", common_type=CommonType.ECOSYSTEM, share=0.15),
            ],
        ),
    ],
    sources=[
        "https://ageoftanks.io/tokenomics/",
    ],
    year=2021,
)
