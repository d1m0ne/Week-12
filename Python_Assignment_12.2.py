import pandas

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/states.csv"
state_data = pandas.read_csv(file_name)

count = 0

for pop in state_data["State"]:
    if pop[0] == "M":
        count += 1

print("The amount of states starting with M is", count)