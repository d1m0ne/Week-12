import pandas

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/states.csv"
state_data = pandas.read_csv(file_name)

pop_list = []

for pop in state_data["Pop"]:
    pop_list.append(pop)
    
pop_list.sort()

print("The Median population density is", pop_list[26])