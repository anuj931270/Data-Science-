# Task: Students Interview Eligibility Checker
Academic_Score=float(input("Enter Academic Score:"))
Attendance_Percentage=float(input("Enter Attendance Percentage:"))
Extracurricular_Participation=input("Enter Extracurricular Participation Name:")
if Academic_Score>=60 and Attendance_Percentage >=75 and Extracurricular_Participation == "Yes":
    print("Eligible for interview")
else:
    print("Not Elegible for interview")