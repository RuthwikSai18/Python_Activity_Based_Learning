#Password policy Validation Engine 
p = input("Enter password: ")
if len(p) >= 8 and any(c.isdigit() for c in p):
    print("Valid Password")
else:
    print("Invalid Password")