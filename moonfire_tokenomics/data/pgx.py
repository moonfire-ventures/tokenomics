from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

pgx = Token(
    token="PGX",
    project="Pegaxy",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Community Developer Incentives", common_type=CommonType.ECOSYSTEM, share=0.16),
                AllocationRecord(type="Ecosystem Reserve and Marketing", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.22),
                AllocationRecord(type="Liquidity Provisions", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Private Sale 1", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Private Sale 2", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="IDO/IEO", common_type=CommonType.PUBLIC_SALE, share=0.02),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.pegaxy.io/in-game-economic-model/governance-token-pgx/pgx-token-allocation-and-unlock-schedule",  # noqa
    ],
    year=2021,
)
