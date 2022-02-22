# 🌓🔥 Tokenomics Research ![Unit Tests](https://github.com/moonfire-ventures/tokenomics/workflows/Unit%20Tests/badge.svg)

This repository contains the code for cryptoeconomics research into the distribution of tokenomics models across several ecosystems that leverage utility and governance tokens for various objectives.

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

## Commit Hooks

Run the following command to manually run pre-commit hooks:

```
pre-commit run --all-files
```