class Account:
    def __init__(self):
        self.__balance = 20000
        self.result = ""
    def deposit(self, amount):
        self.__balance += amount # self.__balance = self.__balance+amount
        self.result = input("Do you want to check balance? y/n ")
        self.result = self.result.lower()
        if self.result == "y":
            self.check_balance()
        else:
            print("Thank you!!")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")
        self.result = input("Do you want to check balance? y/n ")
        self.result = self.result.lower()
        if self.result == "y":
            self.check_balance()
        else:
            print("Thank you!!")
    def check_balance(self):
        print(f"Your balance is {self.__balance}")

acc = Account()
print("Choose your option: \n1.Deposit\n2.Withdraw\n3.Check Balance ")
action = int(input())
if action == 1:
    amount = int(input("Enter amount you want to deposit: "))
    acc.deposit(amount)
elif action == 2:
    amount = int(input("Enter amount you want to withdraw: "))
    acc.withdraw(amount)
elif action == 3:
    acc.check_balance()
else:
    print("Enter a valid option")