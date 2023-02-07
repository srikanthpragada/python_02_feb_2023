num = 19

prime = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        prime = False
        print("Not prime")
        break

if prime:
    print("Prime")
