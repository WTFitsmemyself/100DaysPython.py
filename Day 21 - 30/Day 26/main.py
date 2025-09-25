numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [n+1 for n in numbers]


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
newlist_name = [name.upper() for name in names if len(name) > 5]
print(newlist_name)