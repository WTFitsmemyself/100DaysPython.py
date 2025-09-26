import pandas as pd

student_dict = {
    "student": ["Angela", "John", "Smith"],
    "score": [70, 80, 90]
}


#Loop through dict
# for (student, score) in student_dict.items():
#     print(student)

student_dataframe = pd.DataFrame(student_dict)
# print(student_dataframe)

# for (key, value) in student_dataframe.items():
#     print(key, value)

for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)