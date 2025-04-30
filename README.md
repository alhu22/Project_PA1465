# Pickle Determinism Test Suite

This project tests whether Python's `pickle` module produces identical byte streams (hash-identical) for the same input object.

## How to Run

```bash
pip install -r requirements.txt
PYTHONPATH=. pytest -v
