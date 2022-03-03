from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

gmee = Token(
    token="GMEE",
    project="GAMEE",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Public pre-sale", common_type=CommonType.PUBLIC_SALE, share=0.0016),
                AllocationRecord(type="Private sale", common_type=CommonType.INVESTORS, share=0.0286),
                AllocationRecord(type="Game Operations", common_type=CommonType.ECOSYSTEM, share=0.2528),
                AllocationRecord(type="Strategic Sales", common_type=CommonType.INVESTORS, share=0.0585),
                AllocationRecord(type="Liquidity Pool", common_type=CommonType.TREASURY, share=0.1179),
                AllocationRecord(type="Community Airdrop", common_type=CommonType.AIRDROP, share=0.0094),
                AllocationRecord(type="Marketing & Rewards", common_type=CommonType.ECOSYSTEM, share=0.1255),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Company Reserve", common_type=CommonType.TREASURY, share=0.2057),
            ],
        ),
    ],
    sources=[
        "https://lightpaper.gamee.com/gmee-token/token-allocation",
    ],
    year=2021,
)
