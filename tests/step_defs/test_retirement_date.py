from pytest_bdd import scenario, given, when, then, parsers
from retireeClass import Retiree
import pytest

@scenario('../features/retirement_date.feature', 'get retirement date')
def test_date():
    pass

@pytest.fixture
@given(parsers.parse('retiree was born in {year} in month {month}'))
def retiree(year, month):
    return Retiree(yob=int(year), mob=int(month))

@when("calculate retirement date")
def calc_ret_date(retiree):
    retiree.set_retirement_age()
    retiree.set_retirement_date()

@then(parsers.parse("retirement date is {ret_month} of {ret_year}"))
def retirement_date(retiree, ret_month, ret_year):
    assert retiree.get_retirement_month() == ret_month
    assert retiree.get_retirement_year() == int(ret_year)