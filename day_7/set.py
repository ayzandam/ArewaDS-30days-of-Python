# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
print("Length of the set {}".format(len(it_companies)))

# Add 'Twitter' to it_companies
print("IT companies with Twitter added: {}".format(it_companies.add('Twitter')))

# Insert multiple IT companies at once to the set it_companies
multiples = {'Tiktok', 'Instagram', 'AWS'}
it_companies.update(multiples)
print("Multiple IT companies added: {}".format(it_companies))

# Remove one of the companies from the set it_companies
it_companies.remove('Tiktok')
print("IT companies with Tiktok removed: {}".format(it_companies))

# What is the difference between remove and discard
# Answer:   Remove, eliminate one or more items from a set.
#           And discard completely detroy the set.

# Excercise II
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
print("Set A joined with Set B: {}".format(A.union(B)))

# Find A intersection B
print("Set A joined with Set B: {}".format(A.intersection(B)))

# Is A subset of B
print("Is A subset of B: {}".format(A.issubset(B)))

# Are A and B disjoint sets
print("Are A and B disjoint sets: {}".format(A.isdisjoint(B)))

# Join A with B and B with A
print("Set A joined with Set B: {}".format(A.union(B)))
print("Set B joined with Set A: {}".format(B.union(A)))

# What is the symmetric difference between A and B
print("Symmetric difference between A and B: {}".format(A.symmetric_difference(B)))

# Delete the sets completely
del A, B

# Exercise III

age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Ages set: {}".format(age_set))

# Explain the difference between the following data types: 
# string: combination of characters
# list: combination of one or more elements that can be of the same or different data types, it is mutable
# tuple:combination of one or more elements of the same data type, immutable
# set: combination of one or more elements of the same or different data type, mmutable

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sent = "I am a teacher and I love to inspire and teach people"
tokens = sent.split(' ')
print(sent)
print("Number of words: {}".format(len(tokens)))
print("Number of unique words: {}".format(len(set(tokens))))
