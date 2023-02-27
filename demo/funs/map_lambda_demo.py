nums = [10, 11, 24, 45, 55, 60]

for n in map(lambda n: n + 2 if n % 2 == 0 else n + 1, nums):
    print(n)
