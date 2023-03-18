from datetime import datetime

products = {}
cd = datetime.now()
with open("products.txt", "rt") as f:
    for line in f.readlines():
        try:
            name, ld_str = line.strip().split(",")
            ldate = datetime.strptime(ld_str, "%d-%m-%Y")
            days = (cd - ldate).days
            products[name] = days
        except:
            pass

# Sort dict by values
for name, days in sorted(products.items(), key=lambda t: t[1]):
    print(f"{name:30}   {days:6}")
