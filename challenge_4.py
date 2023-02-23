class Account:
    def __init__(self,title,Balance):
        self.title = title
        self.Balance = Balance



class SavingsAccount(Account):
    def __init__(self,title,Balance,interestRate):
        super().__init__(title,Balance)
        self.interestRate = interestRate



SavingsAccount_obj = SavingsAccount("Ashish",5000,5)
print(SavingsAccount_obj.title)
print(SavingsAccount_obj.Balance)
print(SavingsAccount_obj.interestRate)
