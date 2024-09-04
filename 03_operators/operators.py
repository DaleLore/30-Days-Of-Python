# Declare your age as integer variable
age = 35

# Declare your height as a float variable
height = 1.65 # meters

# Declare a variable that store a complex number
# complex = 2 + a 

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
user_base = input('Enter base: ')
user_height = input('Enter height: ')
area_triangle = int(user_base) * int(user_height) * 0.5
print("The area of the triangle is: " + str(area_triangle))

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle " + str(perimeter))


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input('Enter length: ')
width = input('Enter width: ')
area = int(length) * int(width)
print(area)
permiter = 2 * int(length) + int(width)
print(perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input('Enter radius: ')
pi = 3.14

area = pi * int(radius) ** 2
print(area)

circumference = 2 * pi * int(radius)
print(circumference)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
## Define the coefficients of the line equation y = mx + b
m = 2  # Slope
b = -2  # y-intercept

## Calculate the slope
slope_8 = m

## Calculate the y-intercept
y_intercept = b

## Calculate the x-intercept
x_intercept = -b / m

print(f"Slope: {slope_8}")
print(f"Y-Intercept: {y_intercept}")
print(f"X-Intercept: {x_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
## Define the coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10

## Calculate the slope using the formula (m = (y2 - y1) / (x2 - x1))
slope_9 = (y2 - y1) / (x2 - x1)

## Calculate the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
delta_x_squared = (x2 - x1) ** 2
delta_y_squared = (y2 - y1) ** 2

## Calculate the Euclidean distance by summing the squared differences and taking the square root
distance_squared = delta_x_squared + delta_y_squared
distance = distance_squared ** 0.5

print(f"Slope: {slope_9}")
print(f"Euclidean Distance: {distance}")

# Compare the slopes in tasks 8 and 9.
slope_8 < slope_9
slope_8 > slope_9
slope_8 == slope_9
slope_8 != slope_9

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
>.< algebra 

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
string1 = 'python'
string2 = 'dragon'

len(string1)
len(string2)

## A falsy comparison statement is one that evaluates to False
comparison = string1 < string2

print(f"Is the length of '{string1}' less than the length of '{string2}'? {comparison}")


# Use and operator to check if 'on' is found in both 'python' and 'dragon'


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.


# There is no 'on' in both dragon and python


# Find the length of the text python and convert the value to float and convert it to string


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.


# Check if type of '10' is equal to type of 10


# Check if int('9.8') is equal to 10


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years


# Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''