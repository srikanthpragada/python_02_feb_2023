# Take price and display net price after adding tax

str_price = input("Enter price :")
price = int(str_price)   # convert str to int
tax = price * 0.18
net_price = price + tax
print("Net price =", net_price)

