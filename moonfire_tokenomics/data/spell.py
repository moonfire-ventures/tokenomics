from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

spell = Token(
    name="SPELL",
    project="Abracadabra",
    sector=Sector.DEFI,
    blockchain=[Blockchain.FTM, Blockchain.AVAX, Blockchain.ETH],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="IDO", common_type=CommonType.PUBLIC_SALE, share=0.07),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.3),
                AllocationRecord(type="Farming", common_type=CommonType.ECOSYSTEM, share=0.63),
            ],
        ),
    ],
    sources=[
        "https://docs.abracadabra.money/tokens/tokenomics",
    ],
    year=2021,
)
