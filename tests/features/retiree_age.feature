Feature: Retirement age calculation
  I want to calculate age of retirement for retiree
  Examples:
      | year | month | ret_years | ret_months |
      | 1939 | 3     | 65        | 4          |
      | 1940 | 1     | 65        | 6          |
  Scenario: get retiree age
    Given retiree was born in <year> in month <month>
    When calculate retirement age
    Then retirement age is <ret_years> and <ret_months> months





