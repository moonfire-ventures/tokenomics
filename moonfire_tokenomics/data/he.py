from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

he = Token(
    token="HE",
    project="Heroes & Empires",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=34,
            records=[
                AllocationRecord(type="Strategic Sale", common_type=CommonType.INVESTORS, share=0.15),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.016),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.04),
                AllocationRecord(
                    type="Marketing & Liquidity & Incentives", common_type=CommonType.ECOSYSTEM, share=0.15
                ),
                AllocationRecord(type="Ingame Reward", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="Ecosystem Funds", common_type=CommonType.ECOSYSTEM, share=0.194),
            ],
        ),
    ],
    sources=[
        "https://support.heroesempires.com/hc/en-us/articles/4408399327385-Tokenomics",
    ],
)
