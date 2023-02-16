def avg_length(*values):
    total = 0
    for s in values:
        total += len(s)

    return total // len(values)


print(avg_length("java", "c#", "Python"))
