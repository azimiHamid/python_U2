# with open("./utils_25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("./utils_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempretures = []
#     for row in data:
#         if row[1] != "temp":
#             tempretures.append(int(row[1]))
#     print(tempretures)



import pandas
data = pandas.read_csv("./utils_25/weather_data.csv")
# print(type(data))  # DataFrame
# print(type(data['temp'])) # Series ~ single column, or list
# data['temp'] is a Series here!

data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# total = 0
# for temp in temp_list:
#     total += temp
# avg_temp = round(total / len(temp_list))
# print(avg_temp)

# *********| OR use the SUM() method |*********

temp_list = data['temp'].to_list()
avg_temp = round(sum(temp_list) / len(temp_list))
# print(avg_temp)

# *********| OR use the MEAN() method from PANDAS |*********

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['temp'].median())
# print(data['temp'].min())

# Get Data in Columns
# print(data['condition'])  # Treating like a dictionary
# print(data.condition)     # Treating like an object


# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# Change the Monday tempreture to FARIENHIT
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"{monday_temp_F} F")




# CREATE dataframe FROM SCRATCH
data_dict = {
    "students": ["Hamid", "Sarah", "Hadi"],
    "scores": [78, 76, 88],
}

data = pandas.DataFrame(data_dict)
data.to_csv("utils_25/new_data.csv", index=False)
print(data)