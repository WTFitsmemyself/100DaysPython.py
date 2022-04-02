student_heights = input("Input a list of student heights (seperated by space): ").split()

for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(type(student_heights))
average = (sum(student_heights))/(len(student_heights))
print(type(average))
print(average)