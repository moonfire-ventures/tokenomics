from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

uma = Token(
    name="UMA",
    project="Universal Market Access",
    sector=Sector.DEFI,
    blockchain=[Blockchain.SORA, Blockchain.ETH, Blockchain.AVAX],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="Initial Uniswap listing", common_type=CommonType.PUBLIC_SALE, share=0.02),
                AllocationRecord(type="Future Token Sales", common_type=CommonType.TREASURY, share=0.145),
                AllocationRecord(type="Developers and Users", common_type=CommonType.ECOSYSTEM, share=0.35),
                AllocationRecord(type="Founders and early contributors", common_type=CommonType.TEAM, share=0.335),
                AllocationRecord(type="Investors", common_type=CommonType.INVESTORS, share=0.15),
            ],
        ),
    ],
    sources=[
        "https://dyor-crypto.fandom.com/wiki/UMA_(UMA)#Token_allocation",
    ],
    year=2018,
)
