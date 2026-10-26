# Terminal Record: [Brightline Print Shop]

## 1. Building the project

```
cd Documents/ism3232-midterm
pwd
touch business_rules.py main.py commands.md README.md requirements.txt   
rm requirements.txt
ls -la
python3 -m venv .venv   
source .venv/bin/activate
which python3
pip list
pip install pytest ruff
pip list
pip freeze > requirements.txt
cat requirements.txt
echo '.venv/' > .gitignore 
cat .gitignore
touch tests/__init__.py tests/test_business_rules.py
tree -L 3
tree -L 3 ism3232-midterm
git remote add origin https://github.com/malika-karieva/ism3232-midterm.git
.git
git init
cd Documents/ism3232-midterm
git remote add origin https://github.com/malika-karieva/ism3232-midterm.git
git branch -M main
git push -u origin main
git init
git remote add origin https://github.com/malika-karieva/ism3232-midterm.git
git branch -M main
git push -u origin main
git add .
git commit -m
git status
git add .
git branch -M main 
git push -u origin main
git add .
git commit -m "Initial commit"
git push -u origin main  
code business_rules.py
git status
git add .
git commit -m 'commit' 
git push
git status
git add .
git commit -m 'commit'
git push
code main.py
git status
git add .
git commit -m 'commit'
git push
code main.py
git status
git add .
git commit -m 'commit'
git push
code tests/test_business_rules.py
pytest -v
pytest -v
git status
git add .
git commit -m 'commit'
git push
code commands.md
ruff format .
ruff chech .
pytest -v
git add .
git commit -m 'commit'  
git push
code commands.md
which python3
tree -L 2
cd ..
cd ism3232-midterm
tree -L 2
rg 'def '
rg -l 'print'
rg -l 'print'
rg -l 'print'
ruff format . && ruff check . && pytest -v
git add .
git commit -m 'commit'
git push
git log --oneline
git status
git commit -m 'commit'
git push
code README.md


```

## 2. The virtual environment
``` 
which python3

```

```
/Users/malika/Documents/ism3232-midterm/.venv/bin/python3

```


## 3. The project structure

```
tree -L 2

```
```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

```

## 4. Every function and test
```
rg 'def '

```
```
business_rules.py
19:def calculate_print_cost(copy_price: float, copies: int) -> float:
24:def get_volume_discount(copies: int, student_org: bool = False) -> float:
39:def calculate_job_total(
53:def requires_proof(total: float) -> bool:
58:def needs_overnight_run(copies: int, total: float) -> bool:
63:def total_invoiced(jobs: list) -> float:
73:def largest_job(jobs: list) -> str:
91:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

tests/test_business_rules.py
20:def test_calculate_print_cost_basic():
26:def test_volume_discount_below_mid_tier():
34:def test_volume_discount_at_mid_tier():
40:def test_get_volume_below_top_tier():
46:def test_get_volume_at_top_tier():
52:def test_student_org_changes_volume_discount_answer():
58:def test_calculate_job_total_below_fee_limit():
64:def test_calculate_job_total_at_limit():
70:def test_requires_proof_at_limit():
76:def test_requires_proof_above_limit():
82:def test_needs_overnight_run_copies_at_500_copies():
88:def test_needs_overnight_run_copies_at_520_copies():
94:def test_needs_overnight_run_at_exactly_400_dollars_total():
100:def test_needs_overnight_run_at_exactly_420_dollars_total():
106:def test_total_invoiced_adds_every_job():
116:def test_total_invoiced_of_empy_list_is_zero():
122:def test_largest_job_identifies_highest_total():
137:def test_largest_job_tie_goes_to_the_first():
147:def test_largest_job_of_empty_list_is_empty_string():
153:def test_format_job_line_all_no():

```

## 5. Which files print
```
rg -l 'print'
```
```
business_rules.py
main.py
tests/test_business_rules.py
```
# Note: business_rules.py appears because there is a keyword calculate_print_cost


## 6. The commit history
``` 
git log --oneline
```
```
d062f88 (HEAD -> main, origin/main) commit
5a9ab86 commit
3ecd3c8 commit
1dc9daa commit
c73c64e commit
417db03 commit
03c217b commit
414c723 Initial commit
```