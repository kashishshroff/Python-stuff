#menu driven crud operations on dictionary

def is_key_exist(key,mydict):
    if key in mydict.keys():
        return True
    else:
        return False
    

def valkey(key):
    if not key.isnumeric():
        return "Key should be numeric !"
    
    elif len(key) != 3:
        return "Key should be 3 digits compulsory!"
    
    elif key[0] != '1':
        return "Key should start with 1 !"

    else:
        return True
           
def valname(name):
    if not name.isalpha():
        return "Name should be only Alphabets"
    else:
        return True

def valmark(mark):
    if not mark.isnumeric():
        return "Marks should be numeric"
    
    elif float(mark) not in range(0,101):
        return "Marks should be in range of 1-100"

    else:
        return True
    
    
def insert(key,mydict):
    
    innerdict = {}
    print("Enter Student Information:")

    name = input("Name:")
    if valname(name) == True:
        innerdict["name"] = name.title()
            
        print("Marks:")
        p = input("Physics:")
        
        if valmark(p) == True:
            c = input("Chemistry:")
            
            if valmark(c) == True:
                m = input("Maths:")
                
                if valmark(m) == True:
                    innerdict["Physics"] = float(p)
                    innerdict["Chemistry"] = float(c)
                    innerdict["Maths"] = float(m)
                    
                    mydict[key] = innerdict
                else:
                    print("Maths: " + valmark(m))
            else:
                print("Chemistry: " + valmark(c))
        else:
            print("Physics: " +  valmark(p))
            
                
                    
    else:
        print(valname(name))
        print("INCORRECT TRY AGAIN ! ")
                          





    
def create(mydict):    
    print("CREATE")
    key = input("Enter Rollno: ")
    
    if valkey(key) == True:
        key = int(key)
        if is_key_exist(key,mydict) == False:
            insert(key,mydict)
        
        else:
            print("Roll no doesnt exist")
            print("INCORRECT TRY AGAIN !")   
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")
        

            

def remove(mydict):
    print("REMOVE")
    key = input("Enter Rollno: ")
    
    if valkey(key) == True:
        key = int(key)    
        if is_key_exist(key,mydict) == True:
            print("Deleted item : ")
            print(mydict.pop(key,"INVALID KEY"))
        else:
            print("Roll no doesnt exist")
            print("INCORRECT TRY AGAIN !")
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")

    

def update(mydict):
    print("UPDATE")
    key = input("Enter Rollno: ")
    
    if valkey(key) == True:
        key = int(key)        
        if is_key_exist(key,mydict) == True:
            insert(key,mydict)
        
        else:
            print("Roll no doesnt exist")
            print("INCORRECT TRY AGAIN ! ")      
        
    else:
        print(valkey(key))
        print("INCORRECT TRY AGAIN ! ")
        
        

def display(mydict):
    print("DISPLAY")
    choice = int(input(" 1. DISPLAY ALL \n 2. DISPLAY ONE \n"))
    if choice == 1:
        print("Rollno :          Details       ")
        for key,values in mydict.items():
            print(f"{key} : {values}")
    else:
            
        key = input("Enter Rollno: ")
        
        if valkey(key) == True:
            key = int(key)
            if is_key_exist(key,mydict) == True:
                print(f"{key} : {mydict[key]}")
            
            else:
                print("Roll no doesnt exist")
                print("INCORRECT TRY AGAIN ! ")      
            
        else:
            print(valkey(key))
            print("INCORRECT TRY AGAIN ! ")
            
    
    


def crud():

    mydict = {}
    choice = 1
    
    while True:
        choice = int(input(" 1. CREATE \n 2. REMOVE \n 3. UPDATE \n 4. DISPLAY \n 5. EXIT \n "))
        
        if choice == 1:
            create(mydict)
            
        elif choice == 2:
            remove(mydict)
            
        elif choice == 3:
            update(mydict)            
            
        elif choice == 4:
            display(mydict)
            
        else:
            break
    
crud()
