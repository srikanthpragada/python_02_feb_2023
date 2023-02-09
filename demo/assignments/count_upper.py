# count no. of uppercase letters in a string

st = "This is to TEST"

count = 0
for c in st:
    if c.isupper():
        count += 1

print(count)

