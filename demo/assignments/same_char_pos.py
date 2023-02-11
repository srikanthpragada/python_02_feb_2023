s1 = "abcde"
s2 = "acddf"

for idx, c in enumerate(s1):
    if c == s2[idx]:
        print(idx)
