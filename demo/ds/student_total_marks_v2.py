data = ["1,50", "2,60", "2,66", "1,90", "1,45", "3,50", "5,90"]

students = {}

for entry in data:
    rno, marks = entry.split(",")
    total = students.get(rno, 0)
    students[rno] = total + int(marks)

for rno, total in students.items():
    print(rno, total)
