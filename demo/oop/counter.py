class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value

c = Counter()
c.increment()
c.increment()
print(c.getvalue())


