###7. Define a class Date with data members day, month and year. E.g
##today’s date is 26-09-2024 then the data members will hold following
##values,
##day = 26
##month = 09
##year = 2024
###Overload the operator + to find tomorrow’s date. Consider the given
###date is valid date.


class Date:

    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    
    def __init__(self,day,month,year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def val_date(day,month,year):
        
        while day > 365 or month > 12: 
            while day > months[month]:
                day = day % months[month]
                month = day // months[month]
                #check if day is still > than months[month]

            while month > 12:
                month = month % 12
                year = month // 12
                #check if month is still> than 12
                
        return day,month,year
        

    def __add__(self,other):
        day = self.day + other.day
        month = self.month + other.month
        year = self.year + other.year

        day,month,year = Date.val_date(day,month,year)        


        return Date(day,month,year)


print("Enter day,month,year in dd/mm/yyyy format :")
day = input("")
month = input("")
year = input("")

d1 = Date(day,month,year)
print(f"{d1.day}/{d1.month}/{d1.year}")

print("Enter day,month,year in dd/mm/yyyy format :")
day = input("")
month = input("")
year = input("")

d2 = Date(day,month,year)
print(f"{d2.day}/{d2.month}/{d2.year}")


d3 = d1 + d2
print("ADD d1 + d2 : ")
print(f"{d3.day}/{d3.month}/{d3.year}")
