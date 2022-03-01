from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

axs = Token(
    name="AXS",
    project="Axie Infinity",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.008),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.11),
                AllocationRecord(type="Gaming Issuance", common_type=CommonType.ECOSYSTEM, share=0.0175),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.0167),
                AllocationRecord(type="Sky Mavis", common_type=CommonType.TEAM, share=0.04),
                AllocationRecord(type="Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.03),
            ],
        ),
        Allocation(
            month=65,
            records=[
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.04),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.11),
                AllocationRecord(type="Staking Reward", common_type=CommonType.ECOSYSTEM, share=0.29),
                AllocationRecord(type="Gaming Issuance", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.07),
                AllocationRecord(type="Sky Mavis", common_type=CommonType.TEAM, share=0.21),
                AllocationRecord(type="Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.08),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.axieinfinity.com/axs/allocations-and-unlock",
    ],
    year=2020,
)
