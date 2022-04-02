student_heights = input("Input a list of student heights (seperated by space): ").split()
sum = 0
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i]) #type: ignore
    sum += student_heights[i]   #type: ignore
    
print(round(sum/len(student_heights)))