Feature: Retirement age calculation
  I want to calculate age of retirement for retiree
  Examples:
      | year | month | ret_year | ret_month |
      | 1939 | 3     | 2004       | July      |
      | 1940 | 1     | 2005       | July        |
  Scenario: get retirement date
    Given retiree was born in <year> in month <month>
    When calculate retirement date
    Then retirement date is <ret_month> of <ret_year>