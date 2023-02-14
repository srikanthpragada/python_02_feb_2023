data = ["1,50", "5,60", "2,66", "8,90", "10,45", "1,50", "5,90"]

students = {}

for entry in data:
    rno, marks = entry.split(",")
    if rno in students:
        students[rno] = students[rno] + int(marks);
    else:
        students[rno] = int(marks);


for rno, total in students.items():
    print(rno, total)
