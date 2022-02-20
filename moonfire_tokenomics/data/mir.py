from moonfire_tokenomics.types import (
    Allocation,
    AllocationRecord,
    CommonType,
    Sector,
    Token,
)

mir = Token(
    token="MIR",
    project="Mirror Protocol",
    sector=Sector.DEFI,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="UNI airdrop", common_type=CommonType.AIRDROP, share=0.0247),
                AllocationRecord(type="LUNA airdrop", common_type=CommonType.AIRDROP, share=0.0247),
                AllocationRecord(type="Community Pool", common_type=CommonType.TREASURY, share=0.098),
            ],
        ),
        Allocation(
            month=48,
            records=[
                AllocationRecord(type="UNI airdrop", common_type=CommonType.AIRDROP, share=0.049),
                AllocationRecord(type="LUNA airdrop", common_type=CommonType.AIRDROP, share=0.049),
                AllocationRecord(type="Community Pool", common_type=CommonType.TREASURY, share=0.346),
                AllocationRecord(type="MIR LP Staking reward", common_type=CommonType.ECOSYSTEM, share=0.104),
                AllocationRecord(type="mAsset LP staking reward", common_type=CommonType.ECOSYSTEM, share=0.451),
            ],
        ),
    ],
    sources=[
        "https://docs.mirror.finance/protocol/mirror-token-mir#:~:text=MIR%20will%20be%20distributed%20every,for%20the%20staking%20reward%20distribution.",  # noqa
    ],
)
