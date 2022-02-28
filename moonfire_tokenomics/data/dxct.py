from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

dxct = Token(
    token="DXCT",
    project="DNAxCAT",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.05),
                AllocationRecord(type="NFT Minting", common_type=CommonType.PUBLIC_SALE, share=0.1),
                AllocationRecord(type="Play to Earn", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Partners", common_type=CommonType.INVESTORS, share=0.1),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.15),
                AllocationRecord(type="Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.2),
            ],
        ),
    ],
    sources=[
        "https://dnaxcat.io/?utm_source=DappRadar&utm_medium=deeplink&utm_campaign=visit-website",
    ],
    year=2021,
)
