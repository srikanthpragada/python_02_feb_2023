with open("names.txt", "r") as f:
    for line in f.readlines():
        print(line, end='')

    f.seek(0) # Move to beginning of the file 
    print(f.read())


