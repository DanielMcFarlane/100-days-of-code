# https://docs.python.org/3/tutorial/datastructures.html

# Lists are created using []. Use "" and , to input srings
# the order is determined by the order inputed in the list

# if you wanted to see who joined first
# print(states_of_america[0])
# to count from the end [-1] would be hawaii, [-2] would be alaska etc...

# to alter list
# states_of_america[1] = "Pencilvania"

# to add to the end of a list do .append()
# states_of_america.append("Angelaland")

# to add multple at the end do .extend([new list])
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])


# off by one error index out of range do -1
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states -1])

# you can change the last item via
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# this would print replace Pears with lemons and print ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)