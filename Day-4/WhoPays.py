import random

names = input("Please enter some names (Jack,Nichole,...): ")
name_list = names.split(",")
len_list = len(name_list)
random_index = random.randint(0,len_list)

print(f"{name_list[random_index]} is going to pay for dinner")
