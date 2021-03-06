from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

lrc = Token(
    name="LRC",
    project="Loopring",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH],
    category=[Category.ACCESS],
    capped=True,
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
    year=2017,
)
