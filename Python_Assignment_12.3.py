import pandas

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/states.csv"
state_data = pandas.read_csv(file_name)

state_data["Population Density"] = state_data["Pop"] * state_data["Area"]

print(state_data.head())