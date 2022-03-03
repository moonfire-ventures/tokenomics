from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

bnx = Token(
    name="BNX",
    project="BinaryX",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Genesis mining reward", common_type=CommonType.ECOSYSTEM, share=0.3333),
                AllocationRecord(
                    type="Initial BNX/BUSD trading pair liquidity", common_type=CommonType.TREASURY, share=0.2667
                ),
                AllocationRecord(type="Marketing and LP Reward Reserve", common_type=CommonType.ECOSYSTEM, share=0.3),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://morioh.com/p/906f862b586c",
    ],
    year=2021,
)
