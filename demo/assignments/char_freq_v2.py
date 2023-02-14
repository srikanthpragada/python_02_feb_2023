# Char Freq
st = "how do you do today"

chars = {}
for c in set(st):
    chars[c] = st.count(c)


for c, count in sorted(chars.items()):
    print(c, count)

