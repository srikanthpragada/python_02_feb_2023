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
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient Balance")

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Jack")  # create an object
a1.deposit(10000)
a1.deposit(20000)
a1.withdraw(5000)
print(a1.getbalance())
print(a1.__dict__)
print(a1._Account__balance)

a2 = Account(10, "Mark", 50000)
