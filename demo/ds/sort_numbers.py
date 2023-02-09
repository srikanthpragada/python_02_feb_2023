nums = []

while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    nums.append(num)


for n in sorted(nums):
    print(n, end=' ')
