from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

ampl = Token(
    name="AMPLE",
    project="Ampleforth",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=46,
            records=[
                AllocationRecord(type="Ecosystem", common_type=CommonType.ECOSYSTEM, share=0.232),
                AllocationRecord(type="Seed Investors", common_type=CommonType.INVESTORS, share=0.185),
                AllocationRecord(type="Series A Investors", common_type=CommonType.INVESTORS, share=0.033),
                AllocationRecord(type="IEO", common_type=CommonType.PUBLIC_SALE, share=0.1),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.25),
                AllocationRecord(type="Treasury", common_type=CommonType.TREASURY, share=0.2),
            ],
        ),
    ],
    sources=[
        "https://blog.ampleforth.org/ampleforth-ieo-and-token-distribution-transparency-report-d7b632bbc838",
    ],
    year=2019,
)
