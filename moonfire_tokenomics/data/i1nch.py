from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

i1nch = Token(
    name="1INCH",
    project="1INCH",
    sector=Sector.DEFI,
    blockchain=[Blockchain.BSC, Blockchain.ETH, Blockchain.POLY, Blockchain.AVAX, Blockchain.ONE],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="security of network, maintenance", common_type=CommonType.TREASURY, share=0.30),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.225),
                AllocationRecord(type="Ecosystem growth", common_type=CommonType.ECOSYSTEM, share=0.21),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.195),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.05),
                AllocationRecord(type="Early LPs", common_type=CommonType.AIRDROP, share=0.02),
            ],
        ),
    ],
    sources=[
        "https://blog.1inch.io/1inch-token-and-liquidity-mining-announcement-5a75bad40ded",
    ],
    year=2020,
)
