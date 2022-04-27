student_scores = {
    "Hary": 81,
    "Jim": 44,
    "John": 87,
    "Sara": 81,
    "Ada": 66   
}
Student_Grades = {}

for scores in student_scores:
    Grades = student_scores[scores]
    if Grades > 90 and Grades < 100:
        Student_Grades[scores] = "Outstanding"
    elif Grades > 80 and Grades <= 90:
        Student_Grades[scores] = "Exceeds Expectations"
    elif Grades >= 70 and Grades <= 80:
        Student_Grades[scores] = "Acceptable"
    elif Grades < 70 :
        Student_Grades[scores] = "Fail"

print(Student_Grades)