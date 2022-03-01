from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

badger = Token(
    name="BADGER",
    project="Badger DAO",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Gitcoin", common_type=CommonType.ECOSYSTEM, share=0.02),
                AllocationRecord(type="Liquidity Mining", common_type=CommonType.ECOSYSTEM, share=0.23),
                AllocationRecord(type="Developer Mining", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.15),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="DAO Treasury", common_type=CommonType.TREASURY, share=0.35),
            ],
        ),
    ],
    sources=[
        "https://badgerdao.medium.com/badger-dao-liquidity-mining-launch-b2415301bd31",
    ],
    year=2020,
)
