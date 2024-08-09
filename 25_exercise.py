import pandas

data = pandas.read_csv("./utils_25/Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./utils_25/squirrel_count.csv", index=False)
