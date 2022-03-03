from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

anc = Token(
    token="ANC",
    project="Anchor Protocol",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Luna staking airdrop", common_type=CommonType.AIRDROP, share=0.05),
                AllocationRecord(type="Community Fund", common_type=CommonType.TREASURY, share=0.1),
            ],
        ),
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="Luna staking airdrop", common_type=CommonType.AIRDROP, share=0.05),
                AllocationRecord(type="Community Fund", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.2),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Luna staking rewards", common_type=CommonType.ECOSYSTEM, share=0.1),
                AllocationRecord(type="Borrower incentives", common_type=CommonType.ECOSYSTEM, share=0.4),
                AllocationRecord(type="ANC LP", common_type=CommonType.ECOSYSTEM, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://docs.anchorprotocol.com/protocol/anchor-token-anc",
    ],
    year=2021,
)
