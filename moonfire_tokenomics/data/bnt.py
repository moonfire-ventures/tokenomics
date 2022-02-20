from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

bnt = Token(
    token="BNT",
    project="BANCOR",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="ICO", common_type=CommonType.PUBLIC_SALE, share=0.5),
                AllocationRecord(
                    type="Community Grants, Partnerships & Bounties", common_type=CommonType.ECOSYSTEM, share=0.2
                ),
                AllocationRecord(type="Long-term Foundation Budget", common_type=CommonType.TREASURY, share=0.2),
                AllocationRecord(
                    type="Founders, Team, Advisors & Early Contributors", common_type=CommonType.TEAM, share=0.1
                ),
            ],
        ),
    ],
    sources=[
        "https://bancor.medium.com/bancor-network-token-bnt-contribution-token-creation-terms-48cc85a63812",
    ],
)
