# Create an empty tuple
empty_tuple = tuple()
print("Empty tuple: {}".format(empty_tuple))

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers_tuple = ('Abdullah', 'Ahmad')
print("Brothers tuple: {}".format(brothers_tuple))

sisters_tuple = ('Hassana', 'Fatima')
print("Sisters tuple: {}".format(sisters_tuple))

# Join brothers and sisters tuples and assign it to siblings
siblings_tuple = brothers_tuple + sisters_tuple
print("Siblings tuple: {}".format(siblings_tuple))

# How many siblings do you have?
print("Number of siblings: {}".format(len(siblings_tuple)))

# Modify the siblings tuple and add the name of your father 
# and mother and assign it to family_members
parents_tuple = ('Yakubu', 'Fatima')
family_members = siblings_tuple + parents_tuple
print("Family members: {}".format(family_members))

# Unpack siblings and parents from family_members
siblings, parents = family_members[:4], family_members[4:] 

# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Cabbage', 'Salad')
animal_product = ('Beef', 'Fish')

food_stuff_tp = fruits + vegetables + animal_product

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp )

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = int(len(food_stuff_tp)) - 1
food_stuff_no_middle = food_stuff_lt[::middle]
print(food_stuff_no_middle)

# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_no_three = food_stuff_lt[4:-4]
print(food_stuff_no_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

