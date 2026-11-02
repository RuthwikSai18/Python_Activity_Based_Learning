#Student Performance 
a = int(input("Enter previous marks: "))
b = int(input("Enter current marks: "))
if b > a:
    print("Improvement:", b - a)
elif b < a:
    print("Decline:", a - b)
else:
    print("No change")
if b < 40:
    print("Weak Performance")
elif b >= 75:
    print("Excellent")
else:
    print("Average")
