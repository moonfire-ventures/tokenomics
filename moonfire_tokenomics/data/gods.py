from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

gods = Token(
    name="GODS",
    project="Gods unchained",
    sector=Sector.GAMING,
    blockchain=[Blockchain.ETH, Blockchain.X],
    category=[Category.GOV, Category.PAYMENT],
    capped=True,
    allocations=[
        Allocation(
            month=72,
            records=[
                AllocationRecord(type="Play to Earn Rewards", common_type=CommonType.ECOSYSTEM, share=0.34),
                AllocationRecord(type="Gods Unchained Reserve", common_type=CommonType.TEAM, share=0.25),
                AllocationRecord(type="Community & Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.205),
                AllocationRecord(type="Community allocation", common_type=CommonType.ECOSYSTEM, share=0.07),
                AllocationRecord(type="Token Foundation", common_type=CommonType.TREASURY, share=0.065),
                AllocationRecord(type="Token Sale", common_type=CommonType.PUBLIC_SALE, share=0.07),
            ],
        ),
    ],
    sources=[
        "https://images.godsunchained.com/misc/whitepaper.pdf",
    ],
    year=2021,
)
