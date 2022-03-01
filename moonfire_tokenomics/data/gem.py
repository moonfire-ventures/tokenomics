from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

gem = Token(
    name="GEM",
    project="Guild of Guardians",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="Player Rewards ", common_type=CommonType.ECOSYSTEM, share=0.35),
                AllocationRecord(type="Community Rewards ", common_type=CommonType.ECOSYSTEM, share=0.28),
                AllocationRecord(type="Developers", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Guardians Guild Limited", common_type=CommonType.TEAM, share=0.06),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.06),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.guildofguardians.com/guild-of-guardian-gems/distribution-schedule",
    ],
    year=2021,
)
