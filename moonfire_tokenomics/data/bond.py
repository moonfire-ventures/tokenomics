from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

bond = Token(
    name="BOND",
    project="Barnbridge",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Yield Farming", common_type=CommonType.ECOSYSTEM, share=0.08),
                AllocationRecord(type="Uniswap LP Rewards", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Staking Rewards", common_type=CommonType.ECOSYSTEM, share=0.048),
                AllocationRecord(type="Var Pool Incentives", common_type=CommonType.ECOSYSTEM, share=0.175),
                AllocationRecord(type="Community Reserve", common_type=CommonType.ECOSYSTEM, share=0.177),
                AllocationRecord(type="Core Team", common_type=CommonType.TEAM, share=0.125),
                AllocationRecord(type="DAO Treasury", common_type=CommonType.TREASURY, share=0.1),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.075),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.02),
            ],
        ),
    ],
    sources=[
        "https://barnbridge.com/token-bond/",
    ],
    year=2020,
)
