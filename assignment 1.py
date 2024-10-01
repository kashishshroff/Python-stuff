#Write a Python program to find if the sum of three consecutive numbers in list is 0
#and display all such sequences



list1 = [-1,0,1,0,-1,4]
i = 0

while i< len(list1)-2:
    sum = 0
    sum = list1[i]+list1[i+1]+list1[i+2]
    if sum == 0:
        print(f"{list1[i]}+{list1[i+1]}+{list1[i+2]} = ",sum)          
    i += 1






    
