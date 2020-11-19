import pandas

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/states.csv"
state_data = pandas.read_csv(file_name)

state_data["Population Density"] = state_data["Pop"] * state_data["Area"]

pop_list = []

for pop in state_data["Population Density"]:
    pop_list.append(pop)

pop_list.sort()

print("The largest population density is", pop_list[50])
print("The smallest population density is", pop_list[0])
print("The Median population density is", pop_list[26])