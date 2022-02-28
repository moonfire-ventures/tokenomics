from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

crv = Token(
    token="CRV",
    project="Curve Finance",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="pre-CRV liquidity providers", common_type=CommonType.AIRDROP, share=0.05),
                AllocationRecord(
                    type="Team",
                    common_type=CommonType.TEAM,  # assume 50:50 split between team and investors
                    share=0.15,
                ),
                AllocationRecord(
                    type="Investors",
                    common_type=CommonType.INVESTORS,  # assume 50:50 split between team and investors
                    share=0.15,
                ),
                AllocationRecord(type="Employees", common_type=CommonType.TEAM, share=0.03),
                AllocationRecord(type="Community Reserve", common_type=CommonType.TREASURY, share=0.05),
            ],
        ),
        Allocation(
            month=99,
            records=[
                AllocationRecord(type="pre-CRV liquidity providers", common_type=CommonType.AIRDROP, share=0.05),
                AllocationRecord(type="Liquidity providers", common_type=CommonType.ECOSYSTEM, share=0.57),
                AllocationRecord(
                    type="Team",
                    common_type=CommonType.TEAM,  # assume 50:50 split between team and investors
                    share=0.15,
                ),
                AllocationRecord(
                    type="Investors",
                    common_type=CommonType.INVESTORS,  # assume 50:50 split between team and investors
                    share=0.15,
                ),
                AllocationRecord(type="Employees", common_type=CommonType.TEAM, share=0.03),
                AllocationRecord(type="Community Reserve", common_type=CommonType.TREASURY, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://resources.curve.fi/base-features/understanding-tokenomics",
    ],
    year=2020,
)
