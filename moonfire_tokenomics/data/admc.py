from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

admc = Token(
    token="ADMC",
    project="Adamant Mine",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Game & Rewards", common_type=CommonType.ECOSYSTEM, share=0.64),
                AllocationRecord(type="Airdrop & Beta", common_type=CommonType.AIRDROP, share=0.02),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.02),
                AllocationRecord(type="Devs & Marketing", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="P2PB2B", common_type=CommonType.ECOSYSTEM, share=0.04),  # unclear what this is
                AllocationRecord(type="IDO, Liquidity, Listings", common_type=CommonType.PUBLIC_SALE, share=0.18),
            ],
        ),
    ],
    sources=[
        "https://www.adamantcoin.com/_files/ugd/fe5faa_7f6fb26dc5784085a0e638d7b4acae65.pdf",
    ],
)
