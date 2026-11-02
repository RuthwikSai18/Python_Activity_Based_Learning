#ATM Transaction 
balance = 5000
for i in range(3):
    choice = int(input("1.Deposit  2.Withdraw: "))
    amount = int(input("Enter amount: "))
    if choice == 1:
        balance += amount
    elif choice == 2 and amount <= balance:
        balance -= amount
    else:
        print("Insufficient Balance")
print("Final Balance:", balance)