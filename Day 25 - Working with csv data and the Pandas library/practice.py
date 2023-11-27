# 1. Reading csv using open file
# with open("weather_data.csv") as file:
#     content = file.readlines()
#     stripped_content = []
#     for record in content:
#         stripped_content.append(record.strip())

# print(stripped_content)


# 2. Reading csv using csv library
# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temperature.append(int(row[1]))
#     print(temperature)

# 3. Reading csv using pandas library
# import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()

# print(f"Average temperature: {data['temp'].mean()}")
# print(f"Max temperature: {data['temp'].max()}")

# # Get data in row
# print(data[data.day == 'Monday'])

# # Get data row which has max temperature
# print(data[data.temp == data['temp'].max()])

# # convert monday's temperature into Fahrenheit
# print(f"Monday's temperature: {(data['temp'][0] * 9/5) + 32}")


import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231127.csv")
# Create a new DataFrame with distinct 'Primary Fur Color' values and their counts
fur_color_counts = df['Primary Fur Color'].value_counts().reset_index()
fur_color_counts.columns = ['Fur Color', 'Count']

# Display the resulting DataFrame
print(fur_color_counts)

# Save dataframe as csv
fur_color_counts.to_csv("Fur_Color_Count.csv")