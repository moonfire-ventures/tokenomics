# tokenomics


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