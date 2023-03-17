import re

f = open("story.txt", "rt")
contents = f.read()

words = re.findall(r"\w+", contents)
print(set(words))
