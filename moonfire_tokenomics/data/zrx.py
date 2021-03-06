from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

zrx = Token(
    name="ZRX",
    project="0x",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH, Blockchain.ONE, Blockchain.AVAX],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="ICO", common_type=CommonType.PUBLIC_SALE, share=0.5),
                AllocationRecord(type="Early investors and advisors", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Retained by 0x", common_type=CommonType.TREASURY, share=0.15),
                AllocationRecord(type="Developer Fund", common_type=CommonType.ECOSYSTEM, share=0.15),
            ],
        ),
    ],
    sources=[
        "https://blog.0xproject.com/announcing-the-0x-token-zrx-launch-d4c097d893c7",
    ],
    year=2017,
)
