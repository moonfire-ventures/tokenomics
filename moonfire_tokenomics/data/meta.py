from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

meta = Token(
    name="META",
    project="Metaverse Miner",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Mining", common_type=CommonType.ECOSYSTEM, share=0.7),
                AllocationRecord(type="Private Round", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Eco-fund", common_type=CommonType.TREASURY, share=0.05),
                AllocationRecord(type="Staking Rewards", common_type=CommonType.ECOSYSTEM, share=0.05),
            ],
        ),
    ],
    sources=[
        "https://metaverseminer.medium.com/metaverse-miner-the-hottest-nft-game-3573b853a346",
    ],
    year=2021,
)
