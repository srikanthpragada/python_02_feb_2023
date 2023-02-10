st1 = "how are you"
st2 = "how do you do"

chars = []
for c in st1:
    if c not in chars and c in st2:
        print(c)
        chars.append(c)
