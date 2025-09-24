# with open("weather_data.csv") as weather_data:
#     weather_data_content = weather_data.readlines()
#     print(weather_data_content)

# import csv
import pandas

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
print(data)