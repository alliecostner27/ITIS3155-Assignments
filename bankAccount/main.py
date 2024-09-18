from checkingAccount import checkingAccount
from savingsAccount import savingsAccount

class bankAccount:
    bankName = "Wells Fargo"
   
   # Constructor 
    def __init__(self, customer_name, customer_balance, minimum_Balance):
        self.name = customer_name
        self.balance = customer_balance
        self.minBalance = minimum_Balance
    
    def welcome_message(self):
        print("Hi " +  self.name + ", welcome to " + self.bankName)
        
    def customerInfo(self):
        return "Customer Name: " + self.name + " Balance: " + str(self.balance) + " Minimum Balance: " + str(self.minBalance) + " Bank Name: " + self.bankName
        
    def withdraw(self, withdrawAmount):
        withdrawAmount = float(input("Enter the amount you want to withdraw: "))
        if self.balance - withdrawAmount >= self.minBalance:
            self.balance -= withdrawAmount
            return "Withdrawal successful. Your new balance is: " + str(self.balance)
        else:
            return("Insufficient funds")
    
    def deposit(self, depositAmount):
        depositAmount = float(input("Enter the amount you want to deposit: "))
        self.balance += depositAmount
        return "Deposit successful. Your new balance is: " + str(self.balance)
    
#Creating instance of bankAccount
customer1 = bankAccount("John", 1000, 100)
customer2 = bankAccount("Jane", 2000, 100)
customer3 = checkingAccount("Jack", 3000, 100)

print(customer3.transferLimit(0))
"""
print(customer1.welcome_message())
print(customer1.customerInfo())
print(customer1.withdraw(0))
print(customer1.deposit(0))

print(customer2.welcome_message())
print(customer2.customerInfo())
print(customer2.withdraw(0))
print(customer2.deposit(0))

"""
