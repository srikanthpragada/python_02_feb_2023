import re

f = open("customers.txt", "rt")
customers = {}
for line in f.readlines():
    m = re.search('[a-zA-Z ]+', line)
    # skip line if name not found
    if m is None:
        continue

    name = m.group().strip()
    if len(name) == 0:
        continue

    m = re.search(r'\d+', line)
    # skip line if number not found
    if m is None:
        continue
    mobile = m.group()

    customers[name] = mobile


for name, mobile in sorted(customers.items()):
    print(f"{name:20} {mobile}")
