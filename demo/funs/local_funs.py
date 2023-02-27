g = 100


def f1():
    global g
    g = g + 1
    a = 100
    b = 200

    # local function
    def f2():
        nonlocal a
        a = 200  # using enclosing variable
        b = 300  # create local variable
        print(a, b)

    f2()
    print(a, b)


f1()
