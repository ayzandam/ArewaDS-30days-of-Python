# Declare an empty list
item = list()

# Declare a list with more than 5 items
items = list([2, 0, 8, 4, 5, 7])

# Find the length of your list
print(len(items))

# Get the first item, the middle item and the last item of the list
# First item
print(items[0])

# Middle item
print(items[((((int(len(items)))))/2)-1])

# Last item
print(items[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = list(['Abubakar', 29, 2.5, 'single', 'Ibrahim Aliyu Byepass, Dutse'])

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = list(['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'])

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[(((int(len(it_companies))))/2)-1])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'

# Add an IT company to it_companies
it_companies.append('Twitter')

# Insert an IT company in the middle of the companies list
it_companies.insert('Instagram', ((int(len(it_companies)))/2)-1)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0].upper()

# Join the it_companies with a string '#;  '
print('# '.join(it_companies))

# Check if a certain company exists in the it_companies list.
print('Meta' in it_companies)

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)

# Slice out the first 3 companies from the list
print(it_companies[3:])

# Slice out the last 3 companies from the list
print(it_companies[:3])

# Slice out the middle IT company or companies from the list
print(it_companies[::((((int(len(it_companies)))))/2)-1])

# Remove the first IT company from the list
it_companies.remove('meta')

# Remove the middle IT company or companies from the list
middle = it_companies[(((int(len(it_companies))))/2)-1]
print(it_companies.remove(middle))

# Remove the last IT company from the list
last = it_companies[-1]
print(it_companies.remove(last))

# Remove all IT companies from the list
print(it_companies.clear())

# Destroy the IT companies list
del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)


# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.

full_stack = front_end + back_end
print(full_stack.insert(5, 'Python'))
print(full_stack.insert(6, 'SQL'))

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
print(ages.sort())
print(min(ages))
print(max(ages))

# Add the min age and the max age again to the list
print(ages.add(min(ages)))
print(ages.add(max(ages)))

# Find the average age (sum of all items divided by their number )
print(sum(ages)/len(ages))

# Find the range of the ages (max minus min)
print(max(ages) - min(ages))

# Compare the value of (min - average) and (max - average), use abs() method
avg = abs(sum(ages)/len(ages))

min_avg = min(ages) - avg
max_avg = max(ages) - avg

print("min - avergae is {}".format(min_avg))
print("max - avergae is {}".format(max_avg))

# Find the middle country(ies) in the countries list
countries = [ 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', ]
middle_index = int(len(countries)-1)
print(countries[middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:(middle_index-1)]
second_half = countries[middle_index:]

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
europe = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = europe
print(first)
print(second)
print(third)
print(scandic)