from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

pols = Token(
    name="POLS",
    project="Polkastarter",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Seed sale", common_type=CommonType.INVESTORS, share=0.15),
                AllocationRecord(type="Private sale", common_type=CommonType.INVESTORS, share=0.275),
                AllocationRecord(type="Liquidity Fund", common_type=CommonType.ECOSYSTEM, share=0.225),
                AllocationRecord(type="Marketing Fund", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Team & Advisors", common_type=CommonType.TEAM, share=0.1),
                AllocationRecord(type="Foundational Reserve", common_type=CommonType.TREASURY, share=0.1),
            ],
        ),
    ],
    sources=[
        "https://docs.polkastarter.com/01.-what-is-polkastarter/what-are-the-tokenomics",
    ],
    year=2020,
)
