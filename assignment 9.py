#9 Multiple Inheritance

class Student:
    regno
    name        

    def setRegNo(self):
        return self.s1 + self.s2 + self.s3 + self.s4

    def setName(self):

    def getRegNo(self):

    def getName(self):


class Square(Quad):
    def __init__(self,s1):
        super().__init__(s1,s1,s1,s1)

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return self.s1**2

class Rectangle(Quad):
    def __init__(self,s1,s2):
        super().__init__(s1,s2,s1,s2)

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return self.s1 * self.s2
