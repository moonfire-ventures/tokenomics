from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

tita = Token(
    name="TITA",
    project="Titan Hunters",
    sector=Sector.GAMING,
    blockchain=[Blockchain.BSC],
    category=[Category.GOV, Category.DIVIDEND, Category.PAYMENT],
    capped=True,
    allocations=[
        Allocation(
            month=50,
            records=[
                AllocationRecord(type="Seed Round", common_type=CommonType.INVESTORS, share=0.045),
                AllocationRecord(type="Private Round", common_type=CommonType.INVESTORS, share=0.135),
                AllocationRecord(type="Public Round", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Foundation", common_type=CommonType.ECOSYSTEM, share=0.17),
                AllocationRecord(type="Ecosystem", common_type=CommonType.ECOSYSTEM, share=0.25),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.18),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.titanhunters.io/game-economy/tokenomic",
    ],
    year=2021,
)
