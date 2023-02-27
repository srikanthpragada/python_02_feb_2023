nums = [10, 11, 24, 45, 55, 60]

for n in filter(lambda n: n % 2 == 0, nums):
    print(n)
