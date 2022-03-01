from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

eqz = Token(
    name="EQZ",
    project="Equalizer Finance",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Public Sale/IDO", common_type=CommonType.PUBLIC_SALE, share=0.015),
                AllocationRecord(type="Private Round", common_type=CommonType.INVESTORS, share=0.125),
                AllocationRecord(type="Strateigc Round", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Seed Round", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="TVL Rewards", common_type=CommonType.ECOSYSTEM, share=0.07),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.05),
                AllocationRecord(type="R&D", common_type=CommonType.ECOSYSTEM, share=0.08),
                AllocationRecord(type="Ecosystem Development", common_type=CommonType.ECOSYSTEM, share=0.08),
                AllocationRecord(type="Liquidity Mining", common_type=CommonType.ECOSYSTEM, share=0.05),
                AllocationRecord(type="Yield Farming", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.03),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.equalizer.finance/token/distribution",
    ],
    year=2021,
)
