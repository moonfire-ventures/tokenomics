from distutils.core import setup

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="moonfire_tokenomics",
    version="1.0",
    install_requires=REQUIREMENTS,
    extras_require={
        "testing": ["pytest"],
    },
)
