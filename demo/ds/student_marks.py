data = ["1,50", "5,60", "2,66", "8,90", "10,45"]
students = {}   # empty dict
for entry in data:
    rno, marks = entry.split(",")
    students[int(rno)] = marks

for rno, marks in sorted(students.items()):
    print(rno, marks)





