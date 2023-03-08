from abc import abstractmethod, ABC


# Abstract class
class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print("Name   : ", self.name)
        print("Dept   : ", self.dept)

    def getdept(self):
        return self.dept

    @abstractmethod
    def getsalary(self):
        pass


# Subclass
class ResidentDoctor(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    # Override show() of superclass
    def show(self):
        super().show()
        print("Salary : ", self.salary)

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    # Override show() of superclass
    def show(self):
        super().show()
        print("Visits  : ", self.visits)
        print("Charge  : ", self.charge)

    def getsalary(self):
        return self.visits * self.charge


r = ResidentDoctor("Dr. Joe", "Card", 300000)
r.show()
print(r.getsalary())
c = Consultant("Dr. Jack", "Ped", 10, 1000)
c.show()
print(c.getsalary())

d = Doctor("","")
