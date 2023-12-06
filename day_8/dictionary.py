# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Knight'
dog['color'] = 'Brown'
dog['breed'] = 'African'
dog['legs'] = 4
dog['age'] = 3

# Create a student dictionary and add first_name, last_name, 
# gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first name': 'Bello',
    'last name': 'Muhammad',
    'gender': 'Male',
    'age': 24,
    'marital status': 'Single',
    'skills': ['Coding', 'Analysis', 'Presentation'],
    'country': 'Nigeria',
    'city': 'Adamwa',
    'address': 'Yola North'
}

# Get the length of the student dictionary
print("Length of Student Dictionary: {}".format(len(student)))

# Get the value of skills and check the data type, it should be a list
value = student['skills']
print("The value of skills are: {}".format(value))
print("And the data type is: {}".format(type(value)))

# Modify the skills values by adding one or two skills
student['skills'].append('Problem Solving')
print("Skills after updating: {}".format(student['skills'])) 

# Get the dictionary keys as a list
dkeys = student.keys()
print("Student dictionary keys as a list: {}".format(list(dkeys)))

# Get the dictionary values as a list
dvalues = student.values()
print("Student dictionary values as a list: {}".format(list(dvalues)))

# Change the dictionary to a list of tuples using items() method
print("Dictionary to list using items() method: {}".format(student.items()))

# Delete one of the items in the dictionary
del student['age']
print('Student dictionary with age deleted: {}'.format(student))

# Delete one of the dictionaries
del student