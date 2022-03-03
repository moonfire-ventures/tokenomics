from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

sps = Token(
    token="SPS",
    project="Splinterlands",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=65,
            records=[
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.1333),
                AllocationRecord(type="Foundation/DAO", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.0666),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.09),
                AllocationRecord(type="Partners/Advisors", common_type=CommonType.ADVISORS, share=0.01),
                AllocationRecord(type="Play to Earn", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="Staking/LP/Oracle Rewards", common_type=CommonType.ECOSYSTEM, share=0.3),
            ],
        ),
    ],
    sources=[
        "https://sps.splinterlands.com/distribution",
    ],
    year=2021,
)
