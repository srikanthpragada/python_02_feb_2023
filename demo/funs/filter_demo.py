nums = [10, 11, 24, 45, 55, 60]


def iseven(n : int) -> bool:
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)

for c in filter(str.isupper, "AbcDef"):
    print(c)
