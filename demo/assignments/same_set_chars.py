s1 = "java"
s2 = "ajvaaaa"

result = set(s1) ^ set(s2)
if len(result) > 0:
    print("Different")
else:
    print("Same")

