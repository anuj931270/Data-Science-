# .Task : Student Grading System
marks = float(input("Enter Students Marks:"))
if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")