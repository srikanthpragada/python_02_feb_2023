def table(num, /, length=10):
    for i in range(1, length + 1):
        print(f"{num:3} * {i:2} = {num * i:6}")


table(15, 5)
table(25)
