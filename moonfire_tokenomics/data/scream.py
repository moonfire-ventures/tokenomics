from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

scream = Token(
    name="SCREAM",
    project="Scream",
    sector=Sector.DEFI,
    blockchain=[Blockchain.FTM],
    category=[Category.GOV, Category.DIVIDEND],
    capped=True,
    allocations=[
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="Strategic", common_type=CommonType.INVESTORS, share=0.0036),
                AllocationRecord(type="Seed", common_type=CommonType.INVESTORS, share=0.02),
                AllocationRecord(type="IDO", common_type=CommonType.PUBLIC_SALE, share=0.0175),
                AllocationRecord(type="Rewards", common_type=CommonType.ECOSYSTEM, share=0.5),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Liquidity", common_type=CommonType.ECOSYSTEM, share=0.0125),
                AllocationRecord(type="Treasury", common_type=CommonType.TREASURY, share=0.3464),
            ],
        ),
    ],
    sources=[
        "https://docs.scream.sh/resources/tokenomics",
    ],
    year=2021,
)
