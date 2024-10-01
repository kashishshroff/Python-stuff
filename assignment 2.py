#program to accept number as much as user enters, store in list. Consider all the elements are numbers.
#Store addition of digit of each number till we get single digit number in the list in another list at corresponding position 


mylist1 = []
choice = 'y'
print("Enter number")
while choice == 'y' :
    mylist1.append(int(input("?:")))
    choice = input("continue? y or n")

print("original list : ",mylist1)

mylist2 = []
n1 = 0

for item in mylist1 :
    sum = 0
    while item != 0 :
        n1 = item % 10
        sum += n1
        item = int(item/10)
    mylist2.append(sum)
print("sum of digits list : ",mylist2)


