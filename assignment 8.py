#8. inheritance

class Quad:
    def __init__(self,s1,s2,s3,s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4


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

side = int(input("Enter side: "))
s1 = Square(side)
print("square perimeter : " , s1.perimeter())
print("square area : " , s1.area())


side1 = int(input("Enter side: "))
side2 = int(input("Enter side: "))
r1 = Rectangle(side1,side2)
print("rectangle perimeter : " , r1.perimeter())
print("rectangle area : " , r1.area())
