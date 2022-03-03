from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

dodo = Token(
    token="DODO",
    project="DODO",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=24,
            records=[
                AllocationRecord(type="Community incentives", common_type=CommonType.ECOSYSTEM, share=0.6),
                AllocationRecord(
                    type="Operations/Marketing/Partnerships", common_type=CommonType.ECOSYSTEM, share=0.08
                ),
                AllocationRecord(
                    type="Initial Liquidity Provision (IDO)", common_type=CommonType.PUBLIC_SALE, share=0.01
                ),
                AllocationRecord(type="Core Team/Future Hires/Advisors", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.16),
            ],
        ),
    ],
    sources=[
        "https://blog.dodoex.io/announcing-the-dodo-token-and-initial-dodo-offering-f31b0beb7463",
    ],
    year=2020,
)
