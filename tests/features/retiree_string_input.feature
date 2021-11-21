Feature: String handling for retirement age
  I want to calculate age using string inputs
  Examples:
      | year | month |
      | Nineteen thirty nine | 3     |
      | 1940 | July    |
  Scenario: Error handling strings
    Given retiree was born in <year> in month <month>
    When year or month is not type int
    Then raise type error