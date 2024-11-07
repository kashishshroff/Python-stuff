import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

#CREATE TABLE
##sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
##
##mycursor.execute(sql)
##mydb.commit()

#INSERT
def insert(name,address):
    
    sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
    val = (name,address)
    mycursor.execute(sql,val)
    mydb.commit() #important

    print(mycursor.rowcount, "record inserted.")

#SELECT

def select():

    sql ="SELECT * FROM customers"
    mycursor.execute(sql)
    
    result = mycursor.fetchall()
    for n in result:
        print(n)
    
#UPDATE

def update(scolumn, svalue, wcolumn, wvalue):
    sql = f"UPDATE customers SET {scolumn} = %s WHERE {wcolumn} = %s"
    val = (svalue, wvalue)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record(s) updated")
    
#DELETE

def delete(wcolumn,wvalue):

    sql = f"DELETE FROM customers WHERE {wcolumn} = %s"
    val = (wvalue,)
    mycursor.execute(sql,val)
    mydb.commit()

    print(mycursor.rowcount,"record(s) deleted")

#MAIN---------------------------------------------

def main():

    choice = 1

    while int(choice) <=4:
        choice = input(" 1.Insert \n 2.Select \n 3.Update \n 4.Delete \n 5.Exit \n")
        choice = int(choice)

        if choice == 1:
            
            print("INSERT")
            name = input("Enter name of customer :")
            address = input("Enter address of customer :")
            insert(name,address)
            
        if choice == 2:
            select()
            
        if choice == 3:
            
            print("UPDATE")
            scolumn = input("Enter  SET col of customer :")
            svalue = input("Enter SET value:")

            wcolumn = input("Enter  WHERE col of customer :")
            wvalue = input("Enter  WHERE value:")
            update(scolumn,svalue,wcolumn,wvalue)
            
        if choice == 4:

            print("DELETE")
            wcolumn = input("Enter  WHERE col of customer :")
            wvalue = input("Enter  WHERE value:")
            delete(wcolumn,wvalue)
            
        
main()
