from moonfire_tokenomics.data_types import Allocation, AllocationRecord, CommonType, Sector, Token

fara = Token(
    name="FARA",
    project="Faraland Crystal",
    sector=Sector.GAMING,
    allocations=[
        Allocation(
            month=0,
            records=[
                AllocationRecord(type="Angel Round", common_type=CommonType.INVESTORS, share=0.036),
                AllocationRecord(type="Founding community", common_type=CommonType.INVESTORS, share=0.08),
                AllocationRecord(type="Seed Round", common_type=CommonType.INVESTORS, share=0.02),
                AllocationRecord(type="Private Sale", common_type=CommonType.INVESTORS, share=0.094),
                AllocationRecord(type="Public Sale", common_type=CommonType.PUBLIC_SALE, share=0.01),
                AllocationRecord(type="Advisor & Team", common_type=CommonType.TEAM, share=0.15),
                AllocationRecord(type="Game Incentives", common_type=CommonType.ECOSYSTEM, share=0.22),
                AllocationRecord(type="Marketing & Partnership", common_type=CommonType.ECOSYSTEM, share=0.05),
                AllocationRecord(type="Foundation", common_type=CommonType.ECOSYSTEM, share=0.2),
                AllocationRecord(type="Airdrop", common_type=CommonType.AIRDROP, share=0.03),
                AllocationRecord(type="Liquid & listing", common_type=CommonType.TREASURY, share=0.11),
            ],
        ),
    ],
    sources=[
        "https://faraland.io/static/media/whitepaper.e2c95a2c.pdf",
    ],
    year=2021,
)
