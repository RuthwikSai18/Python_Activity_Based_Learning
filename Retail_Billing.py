#Retail Billing
items = []
total = 0
n = int(input("Enter number of products: "))
for i in range(n):
    price = int(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    bill = price * qty
    items.append(bill)
    total = total + bill
if total >= 5000:
    discount = total * 20 / 100
elif total >= 2000:
    discount = total * 10 / 100
else:
    discount = 0
final = total - discount
print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final)