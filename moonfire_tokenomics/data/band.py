from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

band = Token(
    name="BAND",
    project="Band Protocol",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Seed Sale", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.1237),
                AllocationRecord(type="Ecosystem", common_type=CommonType.ECOSYSTEM, share=0.2563),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.05),
                AllocationRecord(type="Foundation", common_type=CommonType.TREASURY, share=0.22),
            ],
        ),
    ],
    sources=[
        "https://research.binance.com/en/projects/band-protocol",
    ],
    year=2019,
)
