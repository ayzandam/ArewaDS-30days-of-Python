# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 
# 'Thirty Days Of Python'.
challenge = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(challenge))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
challenge = ['Coding', 'For', 'All']
print(' '.join(challenge))

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company.strip('Coding'))

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
task = "Python for Everyone"
print(task.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
task = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(task.split(','))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(len(company)-1)

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
task = "Python For Everyone"
for i in task.split():
    print(i[0])

# Create an acronym or an abbreviation for the name 'Coding For All'.
task = "Coding For All"
for i in task.split():
    print(i[0])

# Use index to determine the position of the first occurrence of C in Coding For All.
task = "Coding For All"
print(task.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
task = "Coding For All"
print(task.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
task = "Coding For All"
print(task.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
task = "You cannot end a sentence with because because because is a conjunction"
print(task.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
task = "You cannot end a sentence with because because because is a conjunction"
print(task.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
task = "You cannot end a sentence with because because because is a conjunction"
print(task.strip('because'))

# Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
task = "You cannot end a sentence with because because because is a conjunction"
print(task.index('because'))

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
task = "You cannot end a sentence with because because because is a conjunction"
print(task.strip('because'))

# Does ''Coding For All' start with a substring Coding?
task = "Coding For All"
print(task.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
task = "Coding For All"
print(task.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# task = "   Coding For All      "
# print(task.split(' ').join(' '))

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
print('30DaysOfPython'.isidentifier())
# thirty_days_of_python
print('thirty_days_of_python'.isidentifier())

# The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
task = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(task))

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \n I just wonder what is next.')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\n')
print('Asabeneh\t250\tFinland\tHelsinki')


# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a, b = 8, 6
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a%b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))