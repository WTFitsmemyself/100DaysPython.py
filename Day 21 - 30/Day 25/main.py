# with open("weather_data.csv") as weather_data:
#     weather_data_content = weather_data.readlines()
#     print(weather_data_content)

# import csv
import pandas

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
# data_list_temp = data["temp"].to_list()
# # print(data_list_temp)
# avg_temp = sum(data_list_temp) / len(data_list_temp)
# print(avg_temp)
# data_mean = data["temp"].mean()
# print(data_mean)
# print(data[data["temp"] == data["temp"].max()])
monday = data[data["day"] == "Monday"]
print(celsius_to_fahrenheit(monday.temp))