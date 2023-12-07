# Exercises: Level 1

# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 
# Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input("Enter your age: "))

if age >= 18:
    print("Your are old enough to learn to drive.")
else:
    print("You need {} more years to learn to drive.".format(18-age))

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:
# Enter your age: 30
# You are 5 years older than me.
your_age = int(input("Enter your age: "))
diff = 28 - your_age
if diff == 0:
    print("We have same age")
elif diff > 0:
    if diff == 1:
        print("I am a year older than you")
    else:
        print("I am {} years older than you".format(diff))
else:
    if diff == -1:
        print("You are a year older than me")
    else:
        print("You are {} years older than me".format(diff))

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, 
# else a is equal to b. 
# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a>b:
    print("{} is greater than {}".format(a, b))
elif a<b:
    print("{} is smaller than {}".format(a, b))
else:
    print("{} is equal to {}".format(a, b))

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-79, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter your score: "))
if score >= 80:
    print("Grade is A")
elif score >= 70 and score < 80:
    print("Grade is B")
elif score >= 60 and score < 70:
    print("Grade is C")
elif score >= 50 and score < 60:
    print("Grade is D")
elif score >= 0 and score < 50:
    print("Grade is F")
else:
    print("Score invalid!")


# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: 
# September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']

month = input("Enter month name: ")
if month in Autumn:
    print("{} is in Autumn Season".format(month))
elif month in Winter:
    print("{} is in Winter Season".format(month))
elif month in Spring:
    print("{} is in Spring Season".format(month))
elif month in Summer:
    print("{} is in Summer Season".format(month))
else:
    print("Invalid Input!")

# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
inp = input("Enter a fruit name: ")
if inp in fruits:
    print("{} is already in the list")
else:
    fruits.append(inp)
    print("{} added to the list".format(inp))

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
#     person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
mid = (int(len(person['skills']))/2)-1
print("Middle skills is {}".format(person['skills'][mid]))

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
status = 'Python' in person['skills']
print("Person has Python Skill") if status else print("Person does not have Python Skill")



