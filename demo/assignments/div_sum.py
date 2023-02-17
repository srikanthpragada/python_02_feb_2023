def div_sum(divisor, *nums):
    total = 0
    for n in nums:
        if n % divisor == 0:
            total += n

    return total


print(div_sum(5, 10, 12, 34, 55))
