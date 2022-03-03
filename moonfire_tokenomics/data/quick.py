from moonfire_tokenomics.types import Allocation, AllocationRecord, CommonType, Sector, Token

quick = Token(
    token="QUICK",
    project="Squickswap",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Liquidity Mining", common_type=CommonType.ECOSYSTEM, share=0.9),
                AllocationRecord(
                    type="UNI Token Holders",
                    common_type=CommonType.AIRDROP,  # assume 50:50 split between team and investors
                    share=0.05,
                ),
                AllocationRecord(
                    type="Team & Advisors",
                    common_type=CommonType.TEAM,  # assume 50:50 split between team and investors
                    share=0.0325,
                ),
                AllocationRecord(type="Future Airdrop", common_type=CommonType.AIRDROP, share=0.01),
                AllocationRecord(type="Marketing", common_type=CommonType.ECOSYSTEM, share=0.0075),
            ],
        ),
    ],
    sources=[
        "https://quickswap-layer2.medium.com/quick-tokenomics-liquidity-mining-details-96-75-distributed-to-the-community-3dbffd6ba214",  # noqa
    ],
)
