from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

srm = Token(
    name="SRM",
    project="Serum",
    sector=Sector.DEFI,
    blockchain=[Blockchain.SOL, Blockchain.TOMO, Blockchain.ETH],
    category=[Category.GOV, Category.DIVIDEND],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Seed and Auction", common_type=CommonType.INVESTORS, share=0.04),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Ecosystem Incentive Fund", common_type=CommonType.ECOSYSTEM, share=0.27),
                AllocationRecord(type="Partner & Collaborator Fund", common_type=CommonType.TREASURY, share=0.27),
                AllocationRecord(type="Project Contributors", common_type=CommonType.ECOSYSTEM, share=0.22),
            ],
        ),
    ],
    sources=[
        "https://www.projectserum.com/serum-token-summary",
    ],
    year=2020,
)
