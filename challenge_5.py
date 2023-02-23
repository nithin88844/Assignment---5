class Account:
    def __init__(self,title,Balance):
        self.title = title
        self.Balance = Balance

    def get_balance(self):
        print("Balance : ",self.Balance)
    
    def deposit(self,amount):
        self.amount = amount
        self.Balance = self.Balance + self.amount

    def withdrawal(self,amount):
        self.amount = amount
        self.Balance = self.Balance - self.amount
        
    



class SavingsAccount(Account):
    def __init__(self,title,Balance,interestRate):
        super().__init__(title,Balance)
        self.interestRate = interestRate

    def interestamount(self):
        int_amount = (self.Balance*self.interestRate)/100
        print("Interest amount : ", int_amount)



SA_obj = SavingsAccount("ashish",5000,5)
SA_obj.get_balance()
SA_obj.deposit( int(input("Enter the amount to deposit : ")))
SA_obj.get_balance()
SA_obj.withdrawal( int(input("Enter the amount to withdraw : ")))
SA_obj.get_balance()
SA_obj.interestamount()