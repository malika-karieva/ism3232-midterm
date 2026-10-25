# test_business_rules.py
# Author: Malika Karieva
# Brightline Print Shop

from business_rules import (
    calculate_print_cost,
    get_volume_discount,
    calculate_job_total,
    requires_proof,
    needs_overnight_run,
    total_invoiced,
    largest_job,
    format_job_line,
)

# Tests


# 1
def test_calculate_print_cost_basic():
    """Tests basic print cost multiplication without discounts."""
    assert round(calculate_print_cost(0.10, 150), 2) == 15.00


# 2
def test_volume_discount_below_mid_tier():
    """Tests Rule 2 mid tier limit side A: 199 copies get 0% discount."""
    assert get_volume_discount(199, False) == 0.0


# 3


def test_volume_discount_at_mid_tier():
    """Tests Rule 2 mid tier limit side B: exactly 200 copies get MID_TIER discount."""
    assert get_volume_discount(200, False) == 0.08


# 4
def test_get_volume_below_top_tier():
    """Tests Rule 2 top tier limit side A: 999 copies stays at MID_TIER discount."""
    assert get_volume_discount(999, False) == 0.08


# 5
def test_get_volume_at_top_tier():
    """Tests Rule 2 top tier limit side B: exactly 1000 copies gets TOP_TIER discount."""
    assert get_volume_discount(1000, False) == 0.15


# 6
def test_student_org_changes_volume_discount_answer():
    """Tests that passing student_org=True adds the extra discount at MID_TIER."""
    assert get_volume_discount(200, student_org=True) == 0.13


# 7
def test_calculate_job_total_below_fee_limit():
    """Tests Rule 4 fee limit side A: base cost $39.75 (< $40.00) adds setup fee."""
    assert round(calculate_job_total(0.25, 159, False), 2) == 54.75


# 8
def test_calculate_job_total_at_limit():
    """Tests Rule 4 fee limit side B: base cost exactly $40.00 skips setup fee."""
    assert round(calculate_job_total(0.25, 160, False), 2) == 40.00


# 9
def test_requires_proof_at_limit():
    """Tests Rule 5 limit side A: exactly $300.00 requires no proof."""
    assert requires_proof(300.00) is False


# 10
def test_requires_proof_above_limit():
    """Tests Rule 5 limit side B: $305.00 requires proof."""
    assert requires_proof(305.00) is True


# 11
def test_needs_overnight_run_copies_at_500_copies():
    """Tests Rule 6 copy limit side A: exactly 500 copies (with a safe total) is False."""
    assert needs_overnight_run(500, 100.00) is False


# 12
def test_needs_overnight_run_copies_at_520_copies():
    """Tests Rule 6 copy limit side B: 520 copies (with a safe total) is True."""
    assert needs_overnight_run(520, 100.00) is True


# 13
def test_needs_overnight_run_at_exactly_400_dollars_total():
    """Tests Rule 6 total limit side A: exactly $400.00 total ( with safe copies) is False."""
    assert needs_overnight_run(100, 400.00) is False


# 14
def test_needs_overnight_run_at_exactly_420_dollars_total():
    """Tests Rule 6 total limit side A: $400.00 total ( with safe copies) is True."""
    assert needs_overnight_run(100, 420.00) is True


# 15
def test_total_invoiced_adds_every_job():
    """Tests total_invoiced computes sum correctly with a short built-in list."""
    test_jobs = [
        {"title": "Flyers", "copy_price": 0.50, "copies": 100, "student_org": False},
        {"title": "Posters", "copy_price": 1.00, "copies": 100, "student_org": False},
    ]
    assert round(total_invoiced(test_jobs), 2) == 150.00


# 16
def test_total_invoiced_of_empy_list_is_zero():
    """Tests total_invoiced returns 0.0 for an empty list."""
    assert total_invoiced([]) == 0.0


# 17
def test_largest_job_identifies_highest_total():
    """Tests largest_job finds the correct job title with the highest total."""
    test_jobs = [
        {
            "title": "Business Cards",
            "copy_price": 0.10,
            "copies": 50,
            "student_org": False,
        },
        {"title": "Brochures", "copy_price": 2.00, "copies": 500, "student_org": False},
    ]
    assert largest_job(test_jobs) == "Brochures"


# 18
def test_largest_job_tie_goes_to_the_first():
    """Tests largest_job behavior when there is a tie between job totals."""
    test_jobs = [
        {"title": "Flyers", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Posters", "copy_price": 1.00, "copies": 100, "student_org": False},
    ]
    assert largest_job(test_jobs) == "Flyers"


# 19
def test_largest_job_of_empty_list_is_empty_string():
    """Tests largest_job returns an empty string when given an empty list"""
    assert largest_job([]) == ""


# 20
def test_format_job_line_all_no():
    line = format_job_line("Flyers", 40.00, False, False)
    assert line == "Flyers: $40.00 | proof: no | overnight run: no"
