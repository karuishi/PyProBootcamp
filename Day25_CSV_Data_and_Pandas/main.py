import pandas as pd

data = pd.read_csv("weather_data.csv")
squirrel_data = pd.read_csv("squirrel_data.csv")
# print(type(data))
# print(type(data["temp"]))

# Transforms to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Transforms to a list
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # Retorns the average value
# print(data["temp"].mean()) 
# # Returns the max value
# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])

# Highest temp row
# print(data[data["temp"] == data["temp"].max()]) # filters the columns with a condition

# def celsius_fahren(celsius):
#     fahren = celsius * 9/5 + 32 
#     return fahren

# # Convert Monday's temp to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# fahren = celsius_fahren(monday_temp)
# print(fahren)

# Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
#print(gray_squirrels)

gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = { 
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")