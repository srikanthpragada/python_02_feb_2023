def first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n

    return None


print(first_even([11, 25, 35, 40, 24]))
print(first_even([11, 25, 35, 55]))
