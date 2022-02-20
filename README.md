# tokenomics


Run the following to be able to run pre-commit hooks before pushing code
```
brew install mypy
brew install pre-commit
```

Manually run pre-commit hooks
```
pre-commit run --all-files
```

Setup python environment & run
```
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .[testing]
```

Run tests
```
pytest tests
```