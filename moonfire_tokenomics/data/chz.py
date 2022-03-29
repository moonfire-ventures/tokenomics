from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

chz = Token(
    name="CHZ",
    project="Chiliz",
    sector=Sector.GAMING,
    blockchain=[Blockchain.ETH],
    category=[Category.PAYMENT, Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Seed investors", common_type=CommonType.INVESTORS, share=0.075),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.05),
                AllocationRecord(type="Advisory Board", common_type=CommonType.ADVISORS, share=0.03),
                AllocationRecord(type="Token sale & pre-sale", common_type=CommonType.INVESTORS, share=0.345),
                AllocationRecord(type="Userbase reserve", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Marketing operations", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Strategic acquisitions", common_type=CommonType.TREASURY, share=0.15),
            ],
        ),
    ],
    sources=[
        "https://www.chiliz.com/en/token-details/",
    ],
    year=2018,
)
