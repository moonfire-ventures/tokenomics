from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

ngl = Token(
    name="NGL",
    project="Gold Fever",
    sector=Sector.GAMING,
    blockchain=[Blockchain.ETH],
    category=[Category.PAYMENT],
    capped=False,
    allocations=[
        Allocation(
            month=36,
            records=[
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Partners & Advisors", common_type=CommonType.ADVISORS, share=0.05),
                AllocationRecord(type="Seed Round", common_type=CommonType.PUBLIC_SALE, share=0.06),
                AllocationRecord(type="Marketing & Acquisition", common_type=CommonType.ECOSYSTEM, share=0.0555),
                AllocationRecord(type="Angel Round", common_type=CommonType.INVESTORS, share=0.038),
                AllocationRecord(type="VC Round", common_type=CommonType.INVESTORS, share=0.1035),
                AllocationRecord(type="SHO", common_type=CommonType.INVESTORS, share=0.0045),
                AllocationRecord(type="Mining", common_type=CommonType.ECOSYSTEM, share=0.4385),
                AllocationRecord(type="Staking & Liquidity", common_type=CommonType.ECOSYSTEM, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://daomaker.com/company/gold-fever#token-economics",
    ],
    year=2021,
)
