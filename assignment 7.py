###7. Define a class Date with data members day, month and year. E.g
##today’s date is 26-09-2024 then the data members will hold following
##values,
##day = 26
##month = 09
##year = 2024
###Overload the operator + to find tomorrow’s date. Consider the given
###date is valid date.


class Date:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __str__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        return 0

    def __add__(self, other):
        if isinstance(other, int) and other == 1:  # We're only adding 1 day
            new_day = self.day + 1
            new_month = self.month
            new_year = self.year

            if new_day > self.days_in_month(new_month, new_year):
                new_day = 1
                new_month += 1
                if new_month > 12:
                    new_month = 1
                    new_year += 1

            return Date(new_day, new_month, new_year)




print("Enter day,month,year in dd/mm/yyyy format :")
day = input("")
month = input("")
year = input("")

today = Date(day,month,year)
tomorrow = today + 1
print(f"Today's date: {today}")
print(f"Tomorrow's date: {tomorrow}")
