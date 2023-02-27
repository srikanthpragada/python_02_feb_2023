# Functions and immutable objects
def zero(n):
    print(id(n))
    n = 0
    print(id(n))


a = 100
print(id(a))
zero(a)
print(a)


# Functions and mutable objects
def prepend(lst, value):
    lst.insert(0, value)


l = [10, 20]
prepend(l, 30)
print(l)
