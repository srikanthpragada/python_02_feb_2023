depts = {}
f = open("employees.txt", "rt")
for line in f.readlines():
    dept, emp, salary = line.split(",")
    if dept in depts:
        employees = depts[dept]  # get value - tuple
        employees[0].append(emp)  # append employee name
        employees[1].append(int(salary))  # append employee salary
    else:
        # new dept so add a new tuple with name and salary
        depts[dept] = ([emp], [int(salary)])

# print(depts)

for dept, employees in depts.items():
    avg = sum(employees[1]) // len(employees[1])
    print(f"{dept:10} {','.join(employees[0]):50} {avg:6}")
