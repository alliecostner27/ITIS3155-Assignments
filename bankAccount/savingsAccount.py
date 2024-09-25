from main import bankAccount

class savingsAccount(bankAccount):
    
    def interestRate(self, interestAmount):
        interestAmount = float(input("Enter the amount you want to deposit: "))
        self.balance += interestAmount
        return "Interest deposited. Your new balance is: " + str(self.balance)