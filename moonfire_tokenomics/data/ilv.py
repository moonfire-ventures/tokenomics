from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

ilv = Token(
    token="ILV",
    project="Illuvium",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=85,
            records=[
                AllocationRecord(type="Pre Seed", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="Seed", common_type=CommonType.INVESTORS, share=0.15),
                AllocationRecord(type="Treasury", common_type=CommonType.TREASURY, share=0.15),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Launchpad", common_type=CommonType.PUBLIC_SALE, share=0.1),
                AllocationRecord(type="Yield Farming", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="In-Game Rewards", common_type=CommonType.ECOSYSTEM, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://docs.illuvium.io/whitepaper/tokenomics/",
    ],
)
