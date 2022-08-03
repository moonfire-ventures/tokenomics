# 🌓🔥 Tokenomics Research ![Unit Tests](https://github.com/moonfire-ventures/tokenomics/workflows/Unit%20Tests/badge.svg)

This repository contains the code for cryptoeconomics research into the distribution of tokenomics models across several ecosystems that leverage utility and governance tokens for various objectives.

The latest version of the tokenomics dataset is always commited to this repository in csv format and can be downloaded [here](https://raw.githubusercontent.com/moonfire-ventures/tokenomics/master/token_allocations.csv).

There is also a UI to explore this data - check out the [Moonfire Tokenomics Explorer](https://tokenomics.moonfire.com/)

# Data Contribution Guidelines

There are currently 2 ways to contribute. You can
1. take matters in your own hands and create a PR (see below); or 
2. raise an issue in this repo with the necessary information (e.g. link to a whitepaper containing token allocation information) and we'll do our best to add it.

If you want to raise a PR yourself please follow these steps:
1. Create a new file under `moonfire_tokenomics/data`
2. In the file, create a new instance of `Token` and fill in the relevant information (see other tokens in this folder)
3. In `moonfire_tokenomics/tokens.py`, import the new token that you created and add it to `Tokens`
4. Run `make dataset` before you commit your changes.


There are tests to ensure that the data you added is correct (for example it checks that token allocations add up to 100%). These tests run automatically and PRs where these tests are failing can't be merged.
We also run automatic style checks, and PRs where these checks are failing can't be merged either. See the sections **Testing** and **Style Checks** below for details and instructions on how to perform these tests locally.

# Development

For development, local Python is managed via [PyEnv](https://github.com/pyenv/pyenv) and its plugin [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv). PyEnv is a tool which lets you easily switch between multiple versions of Python while virtualenv is a tool to create isolated Python environments.

## Setup

To install the appropriate version of Python:

```
pyenv install 3.9.8
```

To setup the virtualenv:

```
pyenv virtualenv 3.9.8 moonfire-tokenomics-3.9.8
```

To activate the virtualenv:

```
pyenv activate moonfire-tokenomics-3.9.8
```

Install the dependencies into the local virtualenv:

```
pip install --upgrade pip
pip install -r requirements.txt
```

Install the modules in your local virtualenv so you can import it from anywhere

```
pip install -e .[testing]
```

The `[testing]` installs additional dev dependencies specified in `setup.py`. At the moment this is only `pytest`. If you're using zsh you have to run `pip install -e ."[testing]"`.

## Testing

To run the tests, run the following command:

```
pytest tests
```

## Style Checks

There are 2 ways to ensure your code passes our automatic style checks.

Ideally you first install the pre-commit hooks  with `pre-commit install`. You can then run the style checks with 
```
pre-commit run --all-files
```

Alternatively you can also run the following commands separately from the root directory.
```
flake8 .
isort .
mypy.
black .
```
