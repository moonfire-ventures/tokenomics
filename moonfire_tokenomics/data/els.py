from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

els = Token(
    name="ELS",
    project="Ethlas",
    sector=Sector.GAMING,
    blockchain=[Blockchain.POLY],
    category=[Category.GOV, Category.DIVIDEND],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="ELS Treasury", common_type=CommonType.TREASURY, share=0.14),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.19),
                AllocationRecord(type="Seed Fundraise", common_type=CommonType.INVESTORS, share=0.145),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.075),
                AllocationRecord(type="Ethlas Builders", common_type=CommonType.TEAM, share=0.215),
                AllocationRecord(type="Ethlas Ecosystem Fund", common_type=CommonType.ECOSYSTEM, share=0.165),
                AllocationRecord(type="Liquidity Pool & Staking rewards", common_type=CommonType.ECOSYSTEM, share=0.07),
            ],
        ),
    ],
    sources=[
        "https://whitepaper.ethlas.com/section-4-tokenomics/usdels-distribution",
    ],
    year=2021,
)
