class Counter:
    count = 0

    @staticmethod
    def getcount():
        return Counter.count

    def __init__(self):
        self.value = 0
        Counter.count += 1

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value


print(Counter.getcount())
c = Counter()
c2 = Counter()
print("Counter objects count ", Counter.getcount())

c.increment()
c.increment()
print(c.getvalue())
