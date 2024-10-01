#operator Overloading. Define a class time with data members , hour and minutes.


class Time:
    hours = 0
    minutes = 0

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes= minutes

    def __add__(self, other):
        minute = self.minutes + other.minutes
        hour = (self.hours + other.hours) + minute // 60
        minute = minute % 60
        return Time(hour, minute)

    def __sub__(self, other):

        minute = self.minutes - other.minutes
        hour = (self.hours - other.hours) + minute // 60
        minute = minute % 60
        return Time(hour, minute)

    def __mul__(self, number):
        minute = self.minutes * number
        hour = (self.hours * number) + minute // 60
        minute = minute % 60
        return Time(hour, minute)

    def printTime(self):
        print(f"Time: {abs(self.hours)} : {abs(self.minutes)}")


#MAIN
hrs = int(input("1 Enter the hour: "))
mins = int(input("1 Enter the min: "))

t1 = Time(hrs, mins)

hrs = int(input("2 Enter the hour: "))
mins = int(input("2 Enter the min: "))
t2 = Time(hrs, mins)

t3 = t1 + t2
t4 = t1 - t2
t5 = t1 * 2
t6 = t2 * 3

print("add : " )
t3.printTime()

print(f"sub : ")
t4.printTime()

print(f"mul to 2 : " )
t5.printTime()

print(f"mul to 3 : " )
t6.printTime()













