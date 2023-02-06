# Take price and display net price after adding tax
# Input
str_price = input("Enter price :")

# Process
price = int(str_price)   # convert str to int
tax = price * 18 // 100
net_price = price + tax

# Output
print(f"Price     : {price:6}")
print(f"+Tax      : {tax:6}")
print(f"Net price : {net_price:6}")

