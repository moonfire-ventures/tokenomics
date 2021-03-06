from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

rune = Token(
    name="RUNE",
    project="THORChain",
    sector=Sector.DEFI,
    blockchain=[Blockchain.BSC],
    category=[Category.PAYMENT],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Service Nodes", common_type=CommonType.ECOSYSTEM, share=0.5),
                AllocationRecord(type="Operational", common_type=CommonType.TREASURY, share=0.13),
                AllocationRecord(type="Community", common_type=CommonType.ECOSYSTEM, share=0.12),
                AllocationRecord(type="Team/Advisors", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Seed", common_type=CommonType.INVESTORS, share=0.06),
                AllocationRecord(type="Pre-sale", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="IDO", common_type=CommonType.INVESTORS, share=0.04),
            ],
        ),
    ],
    sources=[
        "https://medium.com/thorchain/reduction-in-rune-total-supply-a8913adace82",
    ],
    year=2019,
)
