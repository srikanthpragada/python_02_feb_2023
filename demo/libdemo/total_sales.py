f = open("sales.txt", "r")

for line in f.readlines():
    line = line.strip()
    if len(line) == 0:  # blank line
        continue

    parts = line.split(",")
    name = parts[0]
    qtys = filter(str.isdigit, parts[1:])  # ignore non-numbers
    total = sum(map(int, qtys))
    print(f"{name:20} {total:5}")

f.close()
