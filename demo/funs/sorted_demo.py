nums = [-100, -10, 11, -24, 45, 55, 60]

for n in sorted(nums, key=abs):
    print(n, end=' ')
