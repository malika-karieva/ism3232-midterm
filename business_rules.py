# business_rules.py 
# Author: Malika Karieva 
# Brightline Print Shop 

# Business Rule Constants:
MID_TIER_COPIES = 200
TOP_TIER_COPIES = 1000
MID_TIER_DISCOUNT = 0.08
TOP_TIER_DISCOUNT = 0.15
STUDENT_ORG_EXTRA_DISCOUNT = 0.05
SETUP_FEE = 15.00
SET_FEE_THRESHOLD = 40.00
PROOF_THRESHOLD = 300.00
OVERNIGHT_COPIES_THRESHOLD = 500
OVERNIGHT_TOTAL_THRESHOLD = 400.00

# Functions:
def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Returns the print cost before any discount (rule 1)."""
    return copy_price * copies

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Returns the discount rate as a decimal, so 8% is 0.08 (rules 2 and 3)."""
    if copies >= TOP_TIER_COPIES:
        discount = TOP_TIER_DISCOUNT
    elif copies >= MID_TIER_COPIES:
        discount = MID_TIER_DISCOUNT
    else:
        discount = 0.0

    if student_org and copies >= MID_TIER_COPIES:
        discount += STUDENT_ORG_EXTRA_DISCOUNT

    return discount

def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Returns the job total for one job: the discounted cost, plus the setup fee when it applies (rule 4). It must call your first two functions."""
    cost = calculate_print_cost(copy_price, copies)
    discount_rate = get_volume_discount(copies, student_org)
    discounted_cost = cost * (1.0 - discount_rate)

    setup_fee = 0.0
    if discounted_cost < SET_FEE_THRESHOLD:
        setup_fee = SETUP_FEE
    return discounted_cost + setup_fee

def requires_proof(total: float) -> bool:
    """Returns True when the job total requires a printed proof (rule 5), otherwise False."""
    return total > PROOF_THRESHOLD

def needs_overnight_run(copies: int, total: float) -> bool:
    """Returns True when the job needs an overnight press run (rule 6), otherwise False."""
    return copies > OVERNIGHT_COPIES_THRESHOLD or total > OVERNIGHT_TOTAL_THRESHOLD

def total_invoiced(jobs: list) -> float:
    """Returns the sum of the job totals for every job in the list. It must use a for loop that calls calculate_job_total."""
    total = 0.0
    for job in jobs:
        total += calculate_job_total(job["copy_price"], job ["copies"], job ["student_org"])
    return total

def largest_job(jobs: list) -> str:
    """Returns the title of the job with the largest job total. If two are tied for largest, it returns the one that comes first in the list. An empty list returns an empty string, "". It must use a for loop that calls calculate_job_total."""
    if not jobs:
        return ""

    max_total = 0.0
    largest_title = ""

    for job in jobs:
        total = calculate_job_total(job["copy_price"], job["copies"], job["student_org"])
        if total > max_total:
            max_total = total
            largest_title = job["title"]
    return largest_title

def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Returns one line of the report, such as Flyers: $40.00 | proof: no | overnight run: no. Each True/False value is shown as yes or no, and the amount always has two decimal places."""
    proof_text = "no"
    if proof:
        proof_text = "yes"
    
    overnight_text = "no"
    if overnight_run:
        overnight_text = "yes"

    return (
        f"{title}: ${total:.2f} | proof: {proof_text} | overnight run:"
        f"{overnight_text}"
    )

