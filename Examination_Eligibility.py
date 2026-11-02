#Multi stage examination
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
if marks >= 40 and attendance >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible")