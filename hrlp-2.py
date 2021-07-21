import pandas

# selecting specific data and creating a dataframe using the selected data
data = pandas.read_csv("squirrel-data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# creating a dictionary from selected data (count of squirrels based on color)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# convert data_dict (dictionary) into a Dataframe
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel-count.csv")
