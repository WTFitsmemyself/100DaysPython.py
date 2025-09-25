import pandas as pd

data_all = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

list_fur_color = data_all['Primary Fur Color'].to_list()

grey_fur = 0
red_fur = 0
black_fur = 0


for color in list_fur_color:
    if color == "Gray":
        grey_fur += 1
    elif color == "Black":
        black_fur += 1
    elif color == "Cinnamon":
        red_fur += 1

dict_color = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey_fur, red_fur, black_fur]
}

result = pd.DataFrame(dict_color)
print(result)