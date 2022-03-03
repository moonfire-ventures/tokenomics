from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

bcoin = Token(
    token="BCOIN",
    project="Bomb Crypto",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.06),
                AllocationRecord(type="IDO", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Listing Pancakeswap", common_type=CommonType.PUBLIC_SALE, share=0.01),
                AllocationRecord(type="Play to Earn", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Staking Reward", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.06),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.25),
                AllocationRecord(type="Advisor", common_type=CommonType.ADVISORS, share=0.03),
                AllocationRecord(type="DEX Liquidity", common_type=CommonType.TREASURY, share=0.05),
                AllocationRecord(type="Reserves", common_type=CommonType.TREASURY, share=0.12),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.bombcrypto.io/token-allocation",
    ],
)
