from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

atlas = Token(
    name="ATLAS",
    project="Star Atlas",
    sector=Sector.GAMING,
    blockchain=[Blockchain.SOL],
    category=[Category.PAYMENT],
    capped=False,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Public Token Sales", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Listings/Liquidity Pools", common_type=CommonType.ECOSYSTEM, share=0.04),
            ],
        ),
        Allocation(
            month=96,
            records=[
                AllocationRecord(type="Private Token Sales", common_type=CommonType.INVESTORS, share=0.225),
                AllocationRecord(type="Public Pre-Sale", common_type=CommonType.PUBLIC_SALE, share=0.015),
                AllocationRecord(type="Public Token Sales", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Listings/Liquidity Pools", common_type=CommonType.ECOSYSTEM, share=0.04),
                AllocationRecord(type="Rewards/Emission", common_type=CommonType.ECOSYSTEM, share=0.65),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://staratlas.com/economics-paper.pdf",
    ],
    year=2021,
)
