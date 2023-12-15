# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add(num1, num2):
    sum = num1 + num2
    return sum

# Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.

def area():
    r = int(input("Enter radius of the circle: "))
    area = r * r * 3.142
    print("Area of a circle is: ", area)

# Invoking the area function
area()

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    for i in nums:
        if isnumeric(i):
            continue
        else:
            return False
    return True

# Invoking the function
add_all_nums(3, 4, 9)

# Temperature in °C can be converted to °F using this formula: 
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convertTemp():
    temp = float(input("Enter the temperature in celsius:"))
    f = (temp * (9/5)) + 32
    print("Equivalent temperature in Fahrenheit: ", f)

# Invoking the function
convertTemp()

# Write a function called check-season, it takes a month parameter and returns the season: 
# Autumn, Winter, Spring or Summer.
def check_season(month):
    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']
    if month in Autumn:
        return "Autumn"
    elif month in Winter:
        return "Winter"
    elif month in Spring:
        return "Spring"
    elif month in Summer:
        return "Summer"
    else:
        return "Invalid month"

# Invoking and printing the season
print("Season: ", check_season("January"))

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope():
    x1 = int(input("Enter the coordinate of X1: "))
    x2 = int(input("Enter the coordinate of X2: "))
    y1 = int(input("Enter the coordinate of Y1: "))
    y1 = int(input("Enter the coordinate of Y2: "))

    slope = (y2-y1)/(x2-x1)

    return slope

# Invoking the functionand printing the result
print("Slope: ", calculate_slope())

# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def quad_root():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    x1 = b + math.sqrt((b*b) - (4 * a * c))/(2 * a)
    x2 = b - math.sqrt((b*b) - (4 * a * c))/(2 * a)

    print("Roots are X1 = {}, X2 = {}".format(x1, x2))

# Invoking the function
quad_root()

# Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.
def print_list(num = []):
    for i in num:
        print(i)

# Invoking the function
print_list([2, 4, 7, 9])

# Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_list(item = []):
    l = len(item)
    reverse = []
    for i in item:
        reverse.append(item[l-1])
        l = l-1

    return reverse

# Invoking the function
print("Reverse of the list: ", reverse_list([5, 4, 3, 2, 1]))

# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items = []):
    cap = []
    for i in items:
        cap.append(i.capitalize())
    return cap

# Invoking the function
print("Capitalise case: ", capitalize_list_items(["muhammad", "hauwa", "yakubu"]))

# Declare a function named add_item. 
# It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(items = [], item):
    new_items = items.append(item)
    return new_items

# Invoking the function
print("Updated list: ", add_item([2, 9, 7], 2))

# Declare a function named remove_item. 
# It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(items = [], item):
    new_items = items.remove(item)
    return new_items

# Invoking the function
print("Updated list: ", remove_item([2, 9, 7], 2))

# Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_of_numbers(num):
    sum = num
    for i in range(num):
        sum = sum + 1
    print(sum)

# Invoking the function
print("The sum is: ", sum_of_numbers(5))

# Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for i in range(num+1):
        if i%2 != 0:
            sum = sum + i
    print(sum)

# Invoking the function
print("The sum  of all odds is: ", sum_of_odds(5))

# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(num):
    sum = 0
    for i in range(num+1):
        if i%2 == 0:
            sum = sum + i
    print(sum)

# Invoking the function
print("The sum  of all odds is: ", sum_of_evens(5))

# Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(num):
    sum_even = 0
    sum_odd = 0
    for i in range(num+1):
        if i%2 == 0:
            sum_even = sum_even + 1
        else:
            sum_odd = sum_odd + 1
    print("Number of odds are: ", sum_odd)
    print("Number of evens are: ", sum_even)

# Invoking the function
evens_and_odds(100)

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Invoking the function:
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if value is None:
        return True
    else:
        return False

# Example usage:
empty_string = ""

print(f"Is the string empty? {is_empty(empty_string)}")


# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics

def calculate_mean(data):
    return sum(data) / len(data) if data else None

def calculate_median(data):
    return statistics.median(data) if data else None

def calculate_mode(data):
    return statistics.mode(data) if data else None

def calculate_range(data):
    return max(data) - min(data) if data else None

def calculate_variance(data):
    return statistics.variance(data) if data else None

def calculate_std(data):
    return statistics.stdev(data) if data else None

# Example usage:
data_list = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8]

mean_result = calculate_mean(data_list)
median_result = calculate_median(data_list)
mode_result = calculate_mode(data_list)
range_result = calculate_range(data_list)
variance_result = calculate_variance(data_list)
std_result = calculate_std(data_list)

print(f"Mean: {mean_result}")
print(f"Median: {median_result}")
print(f"Mode: {mode_result}")
print(f"Range: {range_result}")
print(f"Variance: {variance_result}")
print(f"Standard Deviation: {std_result}")

# Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage:
test_number = 17

if is_prime(test_number):
    print(f"{test_number} is a prime number.")
else:
    print(f"{test_number} is not a prime number.")


# Write a functions which checks if all items are unique in the list.
def are_all_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

# Example usage:
unique_list = [1, 2, 3, 4, 5]

if are_all_unique(unique_list):
    print("All items in the list are unique.")
else:
    print("Not all items in the list are unique.")

# Write a function which checks if all the items of the list are of the same data type.
def are_all_same_type(lst):
    if not lst:
        return False  # Empty list, no common type
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

# Example usage:
mixed_type_list = [1, 'two', 3.0, [4, 5]]

if are_all_same_type(mixed_type_list):
    print("All items in the list have the same data type.")
else:
    print("Not all items in the list have the same data type.")


# Write a function which check if provided variable is a valid python variable
import re
import keyword

def is_valid_variable(variable_name):
    # Check if the variable name is a Python keyword
    if keyword.iskeyword(variable_name):
        return False

    # Check if the variable name follows the valid Python variable naming convention
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(re.match(pattern, variable_name))

# Example usage:
invalid_variable = "123_invalid"

if is_valid_variable(invalid_variable):
    print(f"{invalid_variable} is a valid Python variable name.")
else:
    print(f"{invalid_variable} is not a valid Python variable name.")

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.