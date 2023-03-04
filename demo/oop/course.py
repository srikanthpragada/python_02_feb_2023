class Course:
    # Static attribute or Class Attribute
    TAXRATE = 18

    @staticmethod   # decorator
    def gettaxrate():
        return Course.TAXRATE

    def __init__(self, title, fee, duration=30):
        # Object Attributes
        self.title = title
        self.fee = fee
        self.duration = duration

    def print(self):
        print(f"Title    :{self.title}")
        print(f"Fee      :{self.fee}")
        print(f"Duration :{self.duration}")

    def getnetfee(self):
        return self.fee + self.fee * Course.TAXRATE // 100


c = Course("AWS", 5000, 20)
c.print()
print(c.getnetfee())

# Call static method
print(Course.gettaxrate())

