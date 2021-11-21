from retireeClass import Retiree

print("Social Security Full Retirement Age Calculator \n")

birth_year = input("Enter the year of birth or press enter to exit: ")
while birth_year:
    birth_month = int(input("Enter the month of birth: "))
    person = Retiree(int(birth_year), int(birth_month))
    person.set_retirement_age()
    person.set_retirement_date()
    print("Your full retirement age is", person.get_retirement_age_years(),"and", person.get_retirement_age_months(),"months")
    print("This will be in", person.get_retirement_month(), "of", person.get_retirement_year())
    birth_year = input("Enter the year of birth or press enter to exit: ")
