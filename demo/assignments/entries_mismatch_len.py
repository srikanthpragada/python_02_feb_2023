l1 = [10, 20, 30, 1, 2, 3]
l2 = [10, 20, 30, 40, 50]

len_l1 = len(l1)
len_l2 = len(l2)

if len_l1 > len_l2:
    l2.extend([None] * (len_l1 - len_l2))
elif len_l2 > len_l1:
    l1.extend([None] * (len_l2 - len_l1))

for v1, v2 in zip(l1, l2):
    print(v1, v2)
