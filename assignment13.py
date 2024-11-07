import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pythondb"
)

mycursor = mydb.cursor()

#Uncomment if you need to create the tables
##sql = """CREATE TABLE department(
##        deptid INT AUTO_INCREMENT PRIMARY KEY,
##        deptname VARCHAR(25), location VARCHAR(50))"""
##mycursor.execute(sql)
##
##sql = """CREATE TABLE employee(
##        empid INT AUTO_INCREMENT PRIMARY KEY,
##        empname VARCHAR(25),
##        salary INT(5),
##        deptid INT,
##        FOREIGN KEY (deptid) REFERENCES department(deptid))"""
##mycursor.execute(sql)

# INSERT function
def insert(table, values):
    
    if table.lower() == 'department':
        sql = "INSERT INTO department (deptname, location) VALUES (%s, %s)"
    elif table.lower() == 'employee':
        sql = "INSERT INTO employee (empname, salary, deptid) VALUES (%s, %s,%s)"
    else:
        print("Invalid table name.")
        return
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")

# SELECT function
def select(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for row in result:
        print(row)

# UPDATE function
def update(table, set_column, set_value, where_column, where_value):
    sql = f"UPDATE {table} SET {set_column} = %s WHERE {where_column} = %s"
    val = (set_value, where_value)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) updated.")

# DELETE function
def delete(table, where_column, where_value):
    sql = f"DELETE FROM {table} WHERE {where_column} = %s"
    val = (where_value,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted.")

#REPORTS    
def generate_reports():
    print("1. List all Employees and their Department Names")
    print("2. List all Departments and their Employee Count")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        query = """SELECT e.empid, e.empname, d.deptname 
                   FROM Employee e 
                   JOIN Department d ON e.deptid = d.deptid"""
        
    elif choice == 2:
        query = """SELECT d.deptid, d.deptname, COUNT(e.empid) 
                   FROM Department d 
                   LEFT JOIN Employee e ON d.deptid = e.deptid 
                   GROUP BY d.deptid, d.deptname"""
    mycursor.execute(query)
    for row in mycursor.fetchall():
        print(row)
# Main Menu
def main():
    while True:
        print("\nCRUD Operations Menu:")
        print("1. Insert")
        print("2. Select")
        print("3. Update")
        print("4. Delete")
        print("5. Reports")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            table = input("Insert into which table (1.department/2.employee): ")

            if table == '1':
                table = 'department'
            if table == '2':
                table = 'employee'
            
            if table == 'department':
                name = input("Enter department name: ")
                location = input("Enter location: ")
                insert(table, (name, location))
                
            elif table == 'employee':
                name = input("Enter employee name: ")
                salary = input("Enter salary: ")
                deptid = input("Enter deptid: ")
                insert(table, (name, salary,deptid))
            else:
                print("Invalid table choice.")
        
        elif choice == '2':
            table = input("Select from which table (1.department/2.employee): ")
            
            if table == '1':
                table = 'department'
            if table == '2':
                table = 'employee'
            select(table)
        
        elif choice == '3':
            table = input("Update which table (department/employee): ")

            if table == '1':
                table = 'department'
            if table == '2':
                table = 'employee'
            
            set_column = input("Enter column to update: ")
            set_value = input("Enter new value: ")
            where_column = input("Enter column for WHERE clause: ")
            where_value = input("Enter value for WHERE clause: ")
            update(table, set_column, set_value, where_column, where_value)
        
        elif choice == '4':
            table = input("Delete from which table (1.department/2.employee): ")

            if table == '1':
                table = 'department'
            if table == '2':
                table = 'employee'
            
            where_column = input("Enter column for WHERE clause: ")
            where_value = input("Enter value for WHERE clause: ")
            delete(table, where_column, where_value)

        elif choice == '5':
            generate_reports()
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")


main()
