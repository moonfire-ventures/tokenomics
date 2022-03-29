from moonfire_tokenomics.data_types import Allocation, AllocationRecord, Blockchain, Category, CommonType, Sector, Token

bag = Token(
    name="BAG",
    project="Bond Appetit",
    sector=Sector.DEFI,
    blockchain=[Blockchain.ETH],
    category=[Category.GOV],
    capped=True,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Pre-launch investors", common_type=CommonType.INVESTORS, share=0.01),
                AllocationRecord(
                    type="Protocol usage & governance participation incentives",
                    common_type=CommonType.ECOSYSTEM,
                    share=0.65,
                ),
                AllocationRecord(type="Team & team members", common_type=CommonType.TEAM, share=0.2),
                AllocationRecord(type="Founders", common_type=CommonType.TEAM, share=0.14),
            ],
        ),
    ],
    sources=[
        "https://bondappetit.io/bag",
    ],
    year=2021,
)
