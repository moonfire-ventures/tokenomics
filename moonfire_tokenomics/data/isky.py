from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

isky = Token(
    name="ISKY",
    project="Infinity Skies",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH],
    category=[Category.PAYMENT],
    capped=True,
    allocations=[
        Allocation(
            month=60,
            records=[
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.01),
                AllocationRecord(type="Seed/Private Sale Allocation", common_type=CommonType.INVESTORS, share=0.25),
                AllocationRecord(type="Play To Earn", common_type=CommonType.ECOSYSTEM, share=0.24),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Company Reserve", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Liquidity Pool", common_type=CommonType.ECOSYSTEM, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://infinityskies.io/whitepaper.pdf",
    ],
    year=2022,
)
