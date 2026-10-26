# ISM3232 Midterm: [Brightline Print Shop]

- **Name:** [Malika Karieva]
- **Version:** [Midterm Practice Exam]
- **Date:** [October 25th 2026]

## What This Program Does
This project prices print shop orders. 'busines_rules.py' turns the company's business rules into eight functions, and 'main.py' runs them over sample print jobs and prints a report: each job's total, the total_invoiced, the largest job, and formatting details. 

## Business Rules
1. The print cost equals the price per copy times the number of copies.
2. 200 - 999 copies get 8% discount; 1000 or more copies get 15% discount.
3. Registered student organizations get an additional 5% discount.
4. When the discounted cost is below $40, a set up fee of $15 is added.
5. If the job total is more than $300, it requires a proof.
6. If there are more than 500 copies or job total is over $400, it needs an overnight press run. 

## How to Run
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test
```
ruff format .
ruff check .
pytest -v
```
The test file has 20 tests, including both sides of every limit
## Files in This Repository
- `business_rules.py`: the constants and the eight functions
- `main.py`: the sample print jobs and a report
- ``tests/test_business_rules.py`: the pytest tests
- `tests/__init__.py`: an empty file that lets the tests import the functions
- ``commands.md`: the terminal commands that built and checked the project, with their output
- `README.md`: this file
- `requirements.txt`: the packages to install
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository

## AI Use Statement
I did not use AI on this exam.