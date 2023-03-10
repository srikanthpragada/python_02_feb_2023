class InsufficientBalanceError(Exception):
     def __init__(self, balance, amount):
         self.balance = balance
         self.amount = amount

     def __str__(self):
         return f"Insufficient Balance {self.balance} for a withdraw of {self.amount}"
class Account:
    # class attribute
    minbal = 5000

    @staticmethod
    def getminbal():
        return Account.minbal

    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.__balance = balance  # Private member

    def deposit(self, amount):
        if amount < 1:
            raise ValueError("Invalid amount for deposit")

        self.__balance += amount

    def withdraw(self, amount):
        if amount < 1:
            raise ValueError("Invalid amount for withdraw")

        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
        else:
            raise InsufficientBalanceError(self.__balance, amount)

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Jack")  # create an object
a1.deposit(10000)
a1.deposit(20000)
a1.withdraw(50000)
print(a1.getbalance())
print(a1.__dict__)
print(a1._Account__balance)

a2 = Account(10, "Mark", 50000)
