class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # private variable

    def deposite(self , amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    

acc = BankAccount(1000)
acc.deposite(500)
print(acc.get_balance()) # 1500
acc.__balance = 0  # cannot modify directly encapsulation prevents this
print(acc.get_balance()) # 1500