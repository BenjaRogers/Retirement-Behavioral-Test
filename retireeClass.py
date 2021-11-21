class Retiree:
    def __init__(self, yob, mob):
        self.yob = yob
        self.mob = mob
        self.retirement_age_years = 0
        self.retirement_age_months = 0
        self.retirement_year = 0
        self.retirement_month = 0


    def set_retirement_age(self):
        if 1900 <= self.yob <= 1937:
            self.retirement_age_years = 65
            self.retirement_age_months = 0
        elif 1938 <= self.yob <= 1942:
            self.retirement_age_years = 65
            self.retirement_age_months = (self.yob - 1937) * 2
        elif 1943 <= self.yob <= 1954:
            self.retirement_age_years = 66
            self.retirement_age_months = 0
        elif 1955 <= self.yob <= 1959:
            self.retirement_age_years = 66
            self.retirement_age_months = (self.yob - 1954) * 2
        elif self.yob >= 1960:
            self.retirement_age_years = 67
            self.retirement_age_months = 0

    def set_retirement_date(self):
        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
                      'December']
        self.retirement_year = self.yob + self.retirement_age_years
        months = self.mob + self.retirement_age_months
        if months > 12:
            self.retirement_year += 1
            months -= 12
        self.retirement_month = month_list[months - 1]

    def get_retirement_age_years(self):
        return self.retirement_age_years

    def get_retirement_age_months(self):
        return self.retirement_age_months

    def get_retirement_year(self):
        return self.retirement_year

    def get_retirement_month(self):
        return self.retirement_month