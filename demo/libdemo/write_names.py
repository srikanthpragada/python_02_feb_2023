f = open("names.txt", "w")

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    f.write(name + "\n")

f.close()
