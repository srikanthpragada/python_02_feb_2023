# Char Freq
st = "how do you do today"

chars = []
for c in st:
    if c not in chars:
        print(c, st.count(c))
        chars.append(c)
