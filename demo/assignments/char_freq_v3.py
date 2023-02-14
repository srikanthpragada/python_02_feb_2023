# Char Freq
st = "how do you do today"

chars = {c: st.count(c) for c in set(st)}

for c, count in sorted(chars.items()):
    print(c, count)
