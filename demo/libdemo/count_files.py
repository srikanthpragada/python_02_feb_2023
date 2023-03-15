import os

stdir = r"d:\classroom\feb2p\demo"
ext = ".py"

allfiles = os.walk(stdir)
count = 0
for (dirname, dirs, files) in allfiles:
    dircount = 0
    for f in files:
        if f.endswith(ext):
            count += 1
            dircount += 1
            print(dirname + "\\" + f)

    print(f"\n{dirname} - {dircount}\n")

print("Total Count = ", count)
