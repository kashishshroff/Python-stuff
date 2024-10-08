class Account:
    # Class variables
    bank_name = "Kotak"
    min_bal = 3000

    def __init__(self, accno: int, name: str, bal: int = 0):
        self.accno = accno
        self.name = name
        
        if bal >= Account.min_bal:
            self.bal = bal
            print(f"Account created successfully for {self.name} with initial balance {self.bal}.")
        else:
            print(f"Minimum balance to open an account is {Account.min_bal}. Account not created.")
            self.bal = 0

    def deposit(self, amt: int) -> int:
        if amt > 0:
            self.bal += amt
            print(f"Successfully deposited {amt}. New balance: {self.bal}.")
            return 1
        else:
            print("Deposit amount must be positive.")
            return 0

    def withdraw(self, amt: int) -> int:
        if amt > 0 and self.bal - amt >= Account.min_bal:
            self.bal -= amt
            print(f"Successfully withdrew {amt}. New balance: {self.bal}.")
            return 1
        else:
            if amt <= 0:
                print("Withdrawal amount must be positive.")
            else:
                print("Insufficient funds. Minimum balance of 3000 must be maintained.")
            return 0

    def check_bal(self) -> str:
        return (f"Bank: {self.bank_name}\n"
                f"Account Number: {self.accno}\n"
                f"Account Holder: {self.name}\n"
                f"Current Balance: {self.bal}")


def valname(name: str) -> bool:
    return name.isalpha()

def valno(mark: str) -> bool:
    return mark.isnumeric()


def insert() -> tuple:
    while True:
        print("ENTER DETAILS:")
        
        accno = input("Enter account number: ")
        if not valno(accno):
            print("Invalid number. Should be Numeric.")
            continue
        accno = int(accno)
        
        name = input("Enter account holder name: ")
        if not valname(name):
            print("Invalid name. Should be Alphabets.")
            continue

        bal = input("Enter starting balance: ")
        if not valno(bal):
            print("Invalid number. Should be Numeric.")
            continue
        bal = int(bal)

        return accno, name, bal


accno, name, bal = insert()
if bal >= Account.min_bal:
    obj1 = Account(accno, name, bal)

    while True:
        choice = int(input("\nMENU: \n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n"))
        if choice == 1:
            amt = int(input("Enter deposit amount: "))
            obj1.deposit(amt)
        elif choice == 2:
            amt = int(input("Enter withdrawal amount: "))
            obj1.withdraw(amt)
        elif choice == 3:
            print(obj1.check_bal())
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")
else:
    print("Account could not be created due to insufficient initial balance.")
    
