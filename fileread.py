#Read the data from file and store it in the dictionary

#file -> employee.txt

# empid department salary


#file = open('employee.txt', 'r')

mydict = {}
with open('employee.txt') as f:
    mylistlines = f.read().splitlines()
    mylist = mylistlines[1].split()

    empid = str(mylist[0])
    department = str(mylist[1])
    salary = str(mylist[2])

    mydict[empid] = { 'department' : department , 'salary' : salary}


for key,values in mydict.items():
    print(f"{key}  {values}")


