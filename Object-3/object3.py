class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.balance = balance
        self.int_rate = int_rate

    @staticmethod
    def convert_to_money(num):
        # return float("%.2f" % round(balance, 2)
        return round(num,2)

    def deposit(self, amount):
        self.balance += amount
        self.balance = BankAccount.convert_to_money(self.balance)


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount


    def display_account_info(self):
        print(f'Balance: ${"%.2f" % round(myAccount.balance,2)}')

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate + 1)
            self.balance = BankAccount.convert_to_money(self.balance)



myAccount = BankAccount(0.20,1000)
print(myAccount.balance)
myAccount.deposit(500)
print(myAccount.balance)
myAccount.withdraw(500)
print(myAccount.balance)
# myAccount.withdraw(1001)
# print(myAccount.balance)
myAccount.yield_interest()
print(myAccount.balance)
myAccount.display_account_info()