import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dictionary = data.to_dict()
print(data_dictionary)

temp_list = data["temp"].to_list()
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
# or
print(data.condition)

# Get Data in a Row
print(data[data.day == "Monday"])

# Get the row data which had highest temperature
print(data[data.temp == data["temp"].max()])

# covert monday temp to fahrenheit
monday = data[data.day == "Monday"]
monday_temp_in_f = (monday.temp * 9 / 5) + 32
print(monday_temp_in_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("student_data.csv")