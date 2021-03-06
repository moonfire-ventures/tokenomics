from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

amp = Token(
    name="AMP",
    project="AMP",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH],
    category=[Category.PAYMENT],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Network Development Fund", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Token Sales", common_type=CommonType.INVESTORS, share=0.2),
                AllocationRecord(type="Founding Team and Employee Pool", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Developer Grants", common_type=CommonType.ECOSYSTEM, share=0.25),
                AllocationRecord(type="Merchant Developer Funf", common_type=CommonType.ECOSYSTEM, share=0.25),
            ],
        ),
    ],
    sources=[
        "https://medium.com/flexa/introducing-flexacoin-b4c8099e3a91",
    ],
    year=2020,
)
