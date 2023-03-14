
f1 = open("names1.txt", "rt")
f2 = open("names2.txt", "rt")

unique_lines = set(f1.readlines()) | set(f2.readlines())
for s in unique_lines:
    print(s.strip())



