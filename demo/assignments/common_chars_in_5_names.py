# get unique chars from all strings
names = ['java', 'pascal', 'javascript', 'fortran', 'ada']

chars = set(names[0])
for n in names:
    chars = chars & set(n)

print(chars)
