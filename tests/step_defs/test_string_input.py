import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from retireeClass import Retiree

@scenario('../features/retiree_string_input.feature', 'Error handling strings')
def test_it():
    pass

@pytest.fixture
@given(parsers.parse('retiree was born in {year} in month {month}'))
def retiree(year, month):
    return Retiree(yob=year, mob=month)


@when("year or month is not type int")
def calc_ret_age(retiree):
    pass


@then(parsers.parse('raise type error'))
def retirement_age(retiree):
    with pytest.raises(TypeError):
        retiree.set_retirement_age()