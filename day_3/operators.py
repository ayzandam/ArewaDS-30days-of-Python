# Day 3 Excercise

# Declare your age as integer variable
age = 29

# Declare your height as a float variable
height = 2.5

# Declare a variable that store a complex number
comp_num = 2+3j

# Write a script that prompts the user to enter base 
# and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input("Enter base: "))
h = int(input("Enter height: "))
area = 0.5 * b * h
print("The area of the triangle is: ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a+b+c

print("The perimeter of the triangle is ", perimeter)

# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area is ", area)
print("Perimeter is ", perimeter)

# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter circle radius: "))
pi = 3.14
area = pi * r * r
c = 2 * pi * r
print("Area is ", area)
print("Circumference is ", c)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("Slope is 2")

# Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1, x2, y1, y2 = 2, 2, 6, 10
slope = (y2-y1)/(x2-x1)
ed = sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))
print("Slope is ", slope)
print("Euclidean distance is ", ed)
# Compare the slopes in tasks 8 and 9.

# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
# x =0
x=0
y = (x ** 2) + 6*x +9
print(f"Value of x = %d, y is %d", x, y)

# x=1
x=1
y = (x ** 2) + 6*x +9
print(f"Value of x = %d, y is %d", x, y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python'))
print(len('dragon'))

print(len('python') == len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in both python and dragon', 'on' in ('python' and 'dragon'))

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon in I hope this course is not full of jargon', ('jargon' in 'I hope this course is not full of jargon'))

# There is no 'on' in both dragon and python
print('There is no on in both dragon and python', ('on' is not ('dragon' and 'python')))

# Find the length of the text python and convert the value to float and convert it to string
l = len('python')

float_l = float(l)
string_l = string(l)

# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
num = int(input("Enter a number"))
if(num%2 == 0):
    print(f"%d is even", num)
else:
    print(f"%d is odd", num)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7//3) is int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') is type(10))

# Check if int('9.8') is equal to 10
print(int('9.8') == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is ", (hours*rate))

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter years: "))
print(f"You have lived for %d seconds", (years * 365 * 24 * 60 *60))

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    l = f"{i} 1 {i} {i*i} {i*i*i}"
    print(l)
