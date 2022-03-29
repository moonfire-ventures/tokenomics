from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

yfi = Token(
    name="YFI",
    project="yearn.finance",
    sector=Sector.DEFI,
    blockchain=[
        Blockchain.ETH,
        Blockchain.FTM,
        Blockchain.AVAX,
        Blockchain.ONE,
        Blockchain.POLY,
        Blockchain.SORA,
        Blockchain.GC,
    ],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Liquidity Providers", common_type=CommonType.ECOSYSTEM, share=1.0),
            ],
        ),
    ],
    sources=[
        "https://www.gemini.com/cryptopedia/what-is-yearn-finance-yfi-coin-yearnfinance#section-what-is-yearn-finance",
    ],
    year=2020,
)
