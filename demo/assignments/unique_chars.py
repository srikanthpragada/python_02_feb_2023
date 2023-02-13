# get unique chars from all strings
names = ['java', 'c#', 'javascript', 'c', 'typescript']

chars = set()
for n in names:
    chars = chars | set(n)
    print(chars)

print(chars)
