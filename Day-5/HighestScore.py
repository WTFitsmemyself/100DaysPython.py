StudentScores = input("Please Input some scores ro calculate: ").split(" ")
max_score = 0

for i in range(0, len(StudentScores)):
    StudentScores[i] = int(StudentScores[i])

for scores in range(0, len(StudentScores)):
    temp = StudentScores[scores]
    if temp > max_score:
        max_score = temp

print(f"{max_score}")