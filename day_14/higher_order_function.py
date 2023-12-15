# Explain the difference between map, filter, and reduce.
# map, filter and reduce are all built-in functions that takes a function and iteratable as paramers
# however, map and filter returns another iterablem while reduce return a value

# Explain the difference between higher order function, closure and decorator

# Define a call function before map, filter or reduce, see examples.

# Use for loop to print each country in the countries list.
countries = [ { "name": "Afghanistan", "capital": "Kabul", "languages": [ "Pashto", "Uzbek", "Turkmen" ], "population": 27657145, "flag": "https://restcountries.eu/data/afg.svg", "currency": "Afghan afghani" }, { "name": "Åland Islands", "capital": "Mariehamn", "languages": [ "Swedish" ], "population": 28875, "flag": "https://restcountries.eu/data/ala.svg", "currency": "Euro" }, { "name": "Albania", "capital": "Tirana", "languages": [ "Albanian" ], "population": 2886026, "flag": "https://restcountries.eu/data/alb.svg", "currency": "Albanian lek" }, { "name": "Algeria", "capital": "Algiers", "languages": [ "Arabic" ], "population": 40400000, "flag": "https://restcountries.eu/data/dza.svg", "currency": "Algerian dinar" }, { "name": "American Samoa", "capital": "Pago Pago", "languages": [ "English", "Samoan" ], "population": 57100, "flag": "https://restcountries.eu/data/asm.svg", "currency": "United State Dollar" }, { "name": "Andorra", "capital": "Andorra la Vella", "languages": [ "Catalan" ], "population": 78014, "flag": "https://restcountries.eu/data/and.svg", "currency": "Euro" }, { "name": "Angola", "capital": "Luanda", "languages": [ "Portuguese" ], "population": 25868000, "flag": "https://restcountries.eu/data/ago.svg", "currency": "Angolan kwanza" }]

# Use for to print each name in the names list.
for name in countries:
    print("Countries names: ", countries['name'])

# Use for to print each number in the numbers list.

# Use map to create a new list by changing each country to uppercase in the countries list
upper = map(lambda name: name.upper(), countries['name'])
print(upper)

# Use map to create a new list by changing each number to its square in the numbers list
# Use map to change each name to uppercase in the names list
# Use filter to filter out countries containing 'land'.
contain_lands = filter(lambda name: 'land' in name, countries['name'])
print(contain_lands)

# Use filter to filter out countries having exactly six characters.
contain_six = filter(lambda name: len(name) == 6, countries['name'])
print(contain_six)

# Use filter to filter out countries containing six letters and more in the country list.
contain_six_more = filter(lambda name: len(name) >= 6, countries['name'])
print(contain_six_more)

# Use filter to filter out countries starting with an 'E'
start_with_e = filter(lambda name: name[0] == 'E', countries['name'])
print(start_with_e)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
from typing import List

def get_string_lists(data: List) -> List:
    return list(filter(lambda item: isinstance(item, str), data))

# Use reduce to sum all the numbers in the numbers list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_result)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]

sentence = reduce(lambda x, y: f"{x}, {y}", countries)
print(sentence + " are north European countries.")

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(countries: List, pattern: str) -> List:
    return list(filter(lambda country: pattern.lower() in country.lower(), countries))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def starting_letter_count(countries: List) -> dict:
    return {country[0]: sum(1 for c in countries if c.startswith(country[0])) for country in countries}

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries: List) -> List:
    return countries[:10]

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries: List) -> List:
    return countries[-10:]

# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
sorted_by_name = sorted(countries, key=lambda x: x["name"])
sorted_by_capital = sorted(countries, key=lambda x: x["capital"])
sorted_by_population = sorted(countries, key=lambda x: x["population"])

print("Sorted by Name:")
print(sorted_by_name)

print("\nSorted by Capital:")
print(sorted_by_capital)

print("\nSorted by Population:")
print(sorted_by_population)

# Sort out the ten most spoken languages by location.
all_languages = [language for country in countries for language in country["languages"]]
language_count = {language: all_languages.count(language) for language in set(all_languages)}

sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("Ten Most Spoken Languages:")
print(sorted_languages)

# Sort out the ten most populated countries.
sorted_by_population = sorted(countries, key=lambda x: x["population"], reverse=True)[:10]

print("Ten Most Populated Countries:")
print(sorted_by_population)
