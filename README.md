# Pytest + Github Actions
[![Coverage Status](coverage.svg)](https://github.com/Jackson-Vieira/pytest-github-ci-example)

This repo is based in the following articles.

- [Automated Python Unit Testing Made Easy with Pytest and GitHub Actions](https://pytest-with-eric.com/integrations/pytest-github-actions/)
- [Automating Build and Tests for Python](https://docs.github.com/pt/actions/automating-builds-and-tests/building-and-testing-python)

## Run

### Requirements
* Python (Python 3.11.5)

check your python with 
```sh
python3 --version or
python --version
```

### How To Run the Unit Tests

Open your terminal and type in

```sh
git clone https://github.com/Jackson-Vieira/pytest-github-ci-example
cd pytest-github-ci-example

# linux
python3 -m venv venv
source venv/bin/active
pip install -r requirements.txt
```

To run the Unit Tests
```commandline
pytest -v -s
```
