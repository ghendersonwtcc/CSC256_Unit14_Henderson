import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from full_retirement_age import full_retirement_age_calc, calculate_final_year

scenarios("./retirement_age_calculator.feature")

@given("User inputs a valid year and valid month")
def retirement_age_year_input():
    # I could not figure out what to put here
    pass


@when(parsers.parse("User inputs year {year} and month {month}"))
def user_input_year_and_month(year):
    retirement_year, retirement_month = full_retirement_age_calc(int(year))

@then(parsers.parse("the calculator should return year {year} and month {month}"))
def user_gets_final_year(year,  month):
    retirement_year, retirement_month = full_retirement_age_calc(1950)
    final_year, final_month = calculate_final_year(1950, 11, retirement_year, retirement_month)
    result = tuple([final_year, final_month])
    assert result == (int(year), int(month))
