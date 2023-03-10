total = 0
for i in range(5):
    try:
        n = int(input("Enter number :"))
        total += n
    except:
        print("Sorry! Invalid Number!")

print(total)
