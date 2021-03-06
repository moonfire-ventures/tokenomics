from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

uni = Token(
    name="UNI",
    project="Uniswap",
    sector=Sector.DEFI,
    blockchain=[
        Blockchain.ETH,
        Blockchain.BSC,
        Blockchain.AVAX,
        Blockchain.ONE,
        Blockchain.POLY,
        Blockchain.SORA,
        Blockchain.GC,
    ],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.15),
                AllocationRecord(type="Liquidity Mining", common_type=CommonType.ECOSYSTEM, share=0.02),
            ],
        ),
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.15),
                AllocationRecord(type="Liquidity Mining", common_type=CommonType.ECOSYSTEM, share=0.02),
                AllocationRecord(type="Governance Treasury", common_type=CommonType.TREASURY, share=0.43),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2151),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.178),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.0069),
            ],
        ),
    ],
    sources=[
        "https://insights.glassnode.com/uni-token-is-uniswap-really-decentralized/",
        "https://uniswap.org/blog/uni",
    ],
    year=2020,
)
