##12. File Handling:
##Accept the data from user as per the data structure given below
##and write it on a file.
##Product = {
##Product_code : [product_name, price, Quantity]
## }
##Accept the data as much as user wants to enter. Write the data on file.
##Filename must be in the format, “Product_dd_mm_yyyy.txt” (The date
##will be current date)
##Write the data on file as will as display it on screen.


Product = {}

choice = '1'

while choice=='1':

    prod_code = int(input("Enter product code :"))
    prod_name = input("Enter product name :")
    prod_price = int(input("Enter product price :"))
    prod_qty = int(input("Enter product quantity :"))

    Product[prod_code] = [prod_name,prod_price,prod_qty]

    choice = input("1/0")


print(Product)  # dict

f = open("demofile.txt", "w")   #create a new text file and open it in write mode
f.write("Product Details\n")
f.write("prod_code|prod_name|prod_price|prod_qty\n")

for key,values in Product.items():
    name,price,qty = values[0],values[1],values[2]
    f.write(f"\t{key}\t|\t{name}\t|\t{price}\t|\t{qty}\n")
f.close()

f = open("demofile.txt", "r")  ##read file dets
print(f.read())
f.close()
    
