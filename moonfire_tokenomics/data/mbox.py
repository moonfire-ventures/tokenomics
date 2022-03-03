from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

mbox = Token(
    name="MBOX",
    project="Mobox",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Strategic Partners", common_type=CommonType.INVESTORS, share=0.08),
                AllocationRecord(type="Contributors", common_type=CommonType.ECOSYSTEM, share=0.21),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Community", common_type=CommonType.ECOSYSTEM, share=0.51),
            ],
        ),
    ],
    sources=[
        "https://research.binance.com/en/projects/mobox",
    ],
    year=2021,
)
