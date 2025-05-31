student_heights = input("Input a list of student heights (seperated by space): ").split()
sumOfAll = 0
lenght = 0

for heights in student_heights:
    lenght += 1

for i in range(0, lenght):
    student_heights[i] = int(student_heights[i]) #type: ignore
    sumOfAll += student_heights[i]   #type: ignore

print(round(sumOfAll/lenght))