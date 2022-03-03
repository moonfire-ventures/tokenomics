from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

byn = Token(
    name="BYN",
    project="Beyond Finance",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Strategic Partners", common_type=CommonType.INVESTORS, share=0.2),
                AllocationRecord(type="Advisors & Team", common_type=CommonType.TEAM, share=0.05),
                AllocationRecord(type="Community Sales", common_type=CommonType.PUBLIC_SALE, share=0.05),
                AllocationRecord(type="Liquidity & Staking Rewards", common_type=CommonType.ECOSYSTEM, share=0.5),
                AllocationRecord(type="Early Contributors", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Marketing & Promotion", common_type=CommonType.ECOSYSTEM, share=0.05),
                AllocationRecord(type="Development Funds", common_type=CommonType.ECOSYSTEM, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://beyondfi.gitbook.io/beyondfi/faq/tokenomics",
    ],
    year=2021,
)
