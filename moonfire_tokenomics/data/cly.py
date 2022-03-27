from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

cly = Token(
    name="CLY",
    project="Colony",
    sector=Sector.DEFI,
    blockchain=[Blockchain.AVAX],
    category=[Category.GOV, Category.DIVIDEND],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.06),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Community Incentives", common_type=CommonType.ECOSYSTEM, share=0.07),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.03),
                AllocationRecord(type="Providing Liquidity", common_type=CommonType.ECOSYSTEM, share=0.1),
                AllocationRecord(type="Seed", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.59),
            ],
        ),
    ],
    sources=[
        "https://medium.com/colony-lab/colonys-core-value-and-tokenomics-explained-1ca8ab0f3b7d",
    ],
    year=2021,
)
