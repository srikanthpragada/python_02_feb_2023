def mathop(a, b, task):
    print(task(a, b))


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


mathop(10, 20, add)
mathop(10, 20, multiply)
#mathop(1, 2, len)   # len takes only 1 param, but we need 2

