#9 Multiple Inheritance

class Student:
    regno
    name        

    def setRegNo(self,regno):
        self.regno = regno
        
    def setName(self,name):
        self.name = name

    def getRegNo(self):
        return self.regno

    def getName(self):
        return self.name

class Exam:
    examno
    pattern
    semister

    def setData(self,examno,pattern,semister):
        self.examno = examno
        self.pattern = pattern
        self.semister = semister

    def getData(self):
        return self.examno,self.pattern,self.semister


class Result(Student,Exam):
    phy
    math
    chem 
    def setMarks(self,phy,math,chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    def getMarks(self):
        return self.phy,self.math,self.chem

    def calResultGrade(self):
        sum = self.phy + self.math + self.chem
        total = 100*3

        perc = sum/total*100
        if perc <= 100 and perc > 80:
            return 'A'
        if perc <= 80 and perc > 60:
            return 'B'
        if perc <= 60 and perc > 40:
            return 'C'
        if perc <= 40 and perc > 20:
            return 'D'
        if perc <= 20:
            return 'F'
        


