from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

mft = Token(
    token="MFT",
    project="Mainframe",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Private sale", common_type=CommonType.INVESTORS, share=0.47),
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.0463),
                AllocationRecord(type="Team", common_type=CommonType.TEAM, share=0.25),
                AllocationRecord(type="Advisors", common_type=CommonType.ADVISORS, share=0.0127),
                AllocationRecord(type="Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.075),
                AllocationRecord(type="Ecosystem Reserve", common_type=CommonType.TREASURY, share=0.146),
            ],
        ),
    ],
    sources=[
        "https://medium.com/flexa/introducing-flexacoin-b4c8099e3a91",
    ],
)
