from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

revv = Token(
    name="REVV",
    project="Revv Motorsport",
    sector=Sector.GAMING,
    blockchain=[Blockchain.ETH, Blockchain.POLY, Blockchain.BSC],
    category=[Category.PAYMENT],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(
                    type="F1® Delta Time - Game Operations", common_type=CommonType.ECOSYSTEM, share=0.17 * 0.5
                ),
                AllocationRecord(type="F1® Delta Time - Staking", common_type=CommonType.ECOSYSTEM, share=0.17 * 0.06),
                AllocationRecord(
                    type="F1® Delta Time - Promotion & Marketing", common_type=CommonType.ECOSYSTEM, share=0.17 * 0.04
                ),
                AllocationRecord(type="F1® Delta Time - Reserve", common_type=CommonType.TREASURY, share=0.17 * 0.4),
                AllocationRecord(type="MotoGP - Ecosystem", common_type=CommonType.ECOSYSTEM, share=0.13),
                AllocationRecord(type="Reserve", common_type=CommonType.TREASURY, share=0.4333),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Initial DEX Offering", common_type=CommonType.PUBLIC_SALE, share=0.0833),
                AllocationRecord(type="Player Reward Reserve", common_type=CommonType.ECOSYSTEM, share=0.0833),
            ],
        ),
    ],
    sources=[
        "https://revvmotorsport.com/",
    ],
    year=2020,
)
