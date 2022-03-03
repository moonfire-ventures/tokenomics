from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

mana = Token(
    name="MANA",
    project="Decentraland",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Foundation", common_type=CommonType.TREASURY, share=0.2),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Community", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Crowdsale", common_type=CommonType.PUBLIC_SALE, share=0.4),
            ],
        ),
    ],
    sources=[
        "https://medium.com/decentraland/the-decentraland-token-sale-terms-81861704c086",
    ],
    year=2017,
)
