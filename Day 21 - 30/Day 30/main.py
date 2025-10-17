try:
    file = open('reza.txt', 'r')
    print(file.read())
    a_dict = {
        'key': 'value',
    }
    print(a_dict['key'])

except FileNotFoundError:
    file = open('reza.txt', 'w')
    file.write('WTF is going on')

except KeyError as k:
    print(f'The key {k} was not found')

else:
    content = file.read()
    print(content)

finally:
    raise ValueError ("Type is not Valid")
    file.close()
    print('File closed')