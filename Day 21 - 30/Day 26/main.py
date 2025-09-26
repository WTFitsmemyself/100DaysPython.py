from random import randint

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [n+1 for n in numbers]


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
newlist_name = [name.upper() for name in names if len(name) > 5]
print(newlist_name)


new_dict = {name:randint(1,100) for name in names}

new_dict_passed = {student:score for (student, score) in new_dict.items() if score >= 60}
print(new_dict_passed)