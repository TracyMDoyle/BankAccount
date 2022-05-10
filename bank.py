class BankAccount:
    Accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.Accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else: 
            self.balance -= self.balance
            print("Insufficient Funds")
        return self

    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        return self
    
    def yield_interest(self, balance):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_accounts(cls):
        for Accounts in cls.Accounts:
            Accounts.display_account_info()


account1 = BankAccount(0.05, 120)
account2 = BankAccount(0.05, 400)

account1.deposit(10).deposit(10).deposit(10).withdraw(5).yield_interest(0.05).display_account_info()
account2.deposit(100).deposit(500).withdraw(250).withdraw(20).withdraw(10).withdraw(20).yield_interest(0.05).display_account_info()

BankAccount.all_accounts()






        
