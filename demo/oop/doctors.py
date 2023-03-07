# Superclass
class Doctor:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print("Name   : ", self.name)
        print("Dept   : ", self.dept)

    def getdept(self):
        return self.dept


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


r = ResidentDoctor("Dr. Joe", "Card", 300000)
r.show()
