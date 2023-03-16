import re

with open(r"d:\classroom\feb2p\test.txt", "rt") as f:
    contents = f.read()

newcontents = re.sub(' +', ' ', contents)   # replace multiple spaces
newcontents = re.sub('\n+', '\n', newcontents ) # replace multiple newlines
print(newcontents)

with open(r"d:\classroom\feb2p\test.txt", "wt") as f:
    f.write(newcontents)
