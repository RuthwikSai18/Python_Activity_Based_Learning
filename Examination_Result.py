#Examination Result
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
if m1 < 35:
    m1 = m1 + 5
if m2 < 35:
    m2 = m2 + 5
if m3 < 35:
    m3 = m3 + 5
total = m1 + m2 + m3
avg = total / 3
print("Total Marks:", total)
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
print("Average:", avg)