
price = int(input("Enter price :"))
if price > 1000:
    discount = price * 20 / 100
else:
    discount = price * 10 / 100

net_price = price - discount
print(net_price)
