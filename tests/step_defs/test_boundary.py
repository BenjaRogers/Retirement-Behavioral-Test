from pytest_bdd import scenario, given, when, then, parsers
from retireeClass import Retiree
import pytest

@scenario('../features/retiree_boundary.feature', 'test boundary')
def test_date():
    pass

@pytest.fixture
@given('retiree was born in 1899 in month 1')
def retiree(year, month):
    return Retiree(yob=1899, mob=1)

@when("calculate retirement date")
def calc_ret_date(retiree):
    retiree.set_retirement_age()

@then('retirement date is None')
def retirement_date(retiree):
    assert retiree.get_retirement_age_years() == None
    assert retiree.get_retirement_age_months() == None