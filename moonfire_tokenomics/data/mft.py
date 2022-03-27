from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

mft = Token(
    name="MFT",
    project="Mainframe",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH],
    category=[Category.GOV],
    capped=True,
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
        "https://hifi.finance/Mainframe-Whitepaper.pdf",
    ],
    year=2018,
)
