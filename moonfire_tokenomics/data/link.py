from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

link = Token(
    name="LINK",
    project="Chainlink",
    sector=Sector.DEFI,
    blockchain=[
        Blockchain.ETH,
        Blockchain.AVAX,
        Blockchain.BSC,
        Blockchain.FTM,
        Blockchain.ONE,
        Blockchain.POLY,
        Blockchain.SORA,
        Blockchain.GC,
    ],
    category=[Category.PAYMENT],
    capped=True,
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
    year=2017,
)
