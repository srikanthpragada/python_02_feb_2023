def squares(end):
    for n in range(1, end + 1):
        yield n * n


s = squares(4)  # Generator
print(next(s))
print(next(s))
print(next(s))

