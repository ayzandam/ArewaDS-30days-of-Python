# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive = [i for i in numbers if i>0]
print(positive)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(flattened_list)

# Using list comprehension create the following list of tuples:
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# Example usage:
print(result)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [(country, capital) for sublist in countries for (country, capital) in sublist]
print(flattened_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list_of_dictionaries = [{country: capital for country, capital in sublist} for sublist in countries]
print(list_of_dictionaries)

# Change the following list of lists to a list of concatenated strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

list_of_strings = [' '.join(name) for sublist in names for name in sublist]
print(list_of_strings)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
# Lambda function to calculate the slope (m) of a linear function
slope_function = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate the y-intercept (b) of a linear function
y_intercept_function = lambda x, y, slope: y - slope * x

# Example usage:
# Given two points (x1, y1) and (x2, y2)
x1, y1 = 1, 2
x2, y2 = 3, 4

slope_result = slope_function(x1, y1, x2, y2)
y_intercept_result = y_intercept_function(x1, y1, slope_result)

print(f"Slope (m): {slope_result}")
print(f"Y-Intercept (b): {y_intercept_result}")
