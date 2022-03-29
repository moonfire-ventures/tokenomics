from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

dydx = Token(
    name="DYDX",
    project="dYdX",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH],
    category=[Category.GOV],
    capped=False,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="User Trading Rewards", common_type=CommonType.ECOSYSTEM, share=0.25),
                AllocationRecord(type="Retroactive Rewards", common_type=CommonType.AIRDROP, share=0.075),
                AllocationRecord(type="Liquidity Provider Rewards", common_type=CommonType.ECOSYSTEM, share=0.1),
                AllocationRecord(type="Community Treasury", common_type=CommonType.TREASURY, share=0.05),
                AllocationRecord(type="Liquidity Staking Pool", common_type=CommonType.ECOSYSTEM, share=0.025),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.2773),
                AllocationRecord(
                    type="Employees & Consultants of dYdX Trading or Foundation",
                    common_type=CommonType.TEAM,
                    share=0.1527,
                ),
                AllocationRecord(
                    type="Futures Employees & Consultants of dYdX Trading or Foundation",
                    common_type=CommonType.TEAM,
                    share=0.07,
                ),
            ],
        ),
    ],
    sources=[
        "https://coin98insights.com/what-is-dydx",
    ],
    year=2020,
)
