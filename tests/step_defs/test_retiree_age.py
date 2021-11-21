import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from retireeClass import Retiree

@scenario('../features/retiree_age.feature', 'get retiree age')
def test_it():
    pass

@pytest.fixture
@given(parsers.parse('retiree was born in {year} in month {month}'))
def retiree(year, month):
    return Retiree(yob=int(year), mob=int(month))


@when("calculate retirement age")
def calc_ret_age(retiree):
    retiree.set_retirement_age()


@then(parsers.parse('retirement age is {ret_years} and {ret_months} months'))
def retirement_age(retiree, ret_years, ret_months):
    assert retiree.get_retirement_age_years() == int(ret_years)
    assert retiree.get_retirement_age_months() == int(ret_months)
