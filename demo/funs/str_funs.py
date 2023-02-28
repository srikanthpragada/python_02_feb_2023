def has_upper(st):
    """
    Returns true if string has an uppercase letter
    :param st: source string
    :return: True or False
    """
    for c in st:
        if c.isupper():
            return True

    return False


def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


# Run this code only when module is run and NOT imported
if __name__ == '__main__':
    print(has_upper('abc'), has_upper('A'))
    print(count_upper('abc'), count_upper('ABC'))
