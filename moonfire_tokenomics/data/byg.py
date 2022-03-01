from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

byg = Token(
    name="BYG",
    project="Black Eye Galaxy",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Seed Sale", common_type=CommonType.INVESTORS, share=0.02),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.015),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.099),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.039),
                AllocationRecord(type="Treasury", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Liquidity", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(
                    type="Distributed as planet resources to be mined", common_type=CommonType.ECOSYSTEM, share=0.321
                ),
                AllocationRecord(type="Staking to support liquidity", common_type=CommonType.ECOSYSTEM, share=0.1),
                AllocationRecord(type="PR", common_type=CommonType.ECOSYSTEM, share=0.005),
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.001),
            ],
        ),
    ],
    sources=[
        "https://www.blackeyegalaxy.space/?utm_source=DappRadar&utm_medium=deeplink&utm_campaign=visit-website",
    ],
    year=2021,
)
