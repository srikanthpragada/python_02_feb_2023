class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Joe", 25)
print(int(p1)) # p1.__int__()

p2 = Person("Andy", 30)
p3 = Person("Joe", 25)

print(p1)  # p1.__str__()
print(p1 == p3)  # p1.__eq__(p3)
# print(p1 > p2)  # p1.__gt__(p2)

people = [p1, p2, p3, Person("Jack", 28)]
for p in sorted(people):
    print(p)
