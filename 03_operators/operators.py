#1 Declare your age as integer variable
age = 35

#2 Declare your height as a float variable
height = 1.65 # meters

#3 Declare a variable that store a complex number
print('Complex number: ', 1 + 1j)

#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
user_base = input('Enter base: ')
user_height = input('Enter height: ')
area_triangle = int(user_base) * int(user_height) * 0.5
print("The area of the triangle is: " + str(area_triangle))

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle " + str(perimeter))


#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input('Enter length: ')
width = input('Enter width: ')
area = int(length) * int(width)
print(area)
permiter = 2 * int(length) + int(width)
print(perimeter)

#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input('Enter radius: ')
pi = 3.14

area = pi * int(radius) ** 2
print('Area of a circle:', area)

circumference = 2 * pi * int(radius)
print(circumference)


#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
## slope formula y = mx + b
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

#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
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

#10 Compare the slopes in tasks 8 and 9.
slope_8 < slope_9
slope_8 > slope_9
slope_8 == slope_9
slope_8 != slope_9

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
## quadratic equation (¬⤙¬ )
### Define a range of x values to test
x_values = range(-5, 5)

### Calculate and check y for each x value
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print(f"y = 0 when x = {x}")
        break

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
string1 = 'python'
string2 = 'dragon'

len(string1)
len(string2)

## Option 1: A falsy comparison statement is one that evaluates to False
comparison = string1 < string2
print(f"Is the length of '{string1}' less than the length of '{string2}'? {comparison}")

## Option 2: Use not to automatically make falsy
print(not len('python') == len('dragon'))

#13 Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#14 'I hope this course is not full of jargon.' Use 'in' operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

#15 There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#16 Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
## Remember that modulus gives us the remainder of a division operation. So if we want 0
are_you_even = int(input('Enter number: '))
print("Even" if are_you_even % 2 == 0 else "Odd")

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
## Perform floor division
floor_division_result = 7 // 3

## Convert float to integer
int_conversion_result = int(2.7)

## Compare the results
is_equal = floor_division_result == int_conversion_result
print(is_equal)

#19 Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#20 Check if int('9.8') is equal to 10
## It will yell at you for attempting to convert a string with a decimal value, such as '9.8', directly to an integer using int() will result in a ValueError because int() does not handle floating-point numbers.
## print(int('9.8') == 10)

## First convert the string to a float and then to an integer
value = int(float('9.8'))

## Then check and compare
result = (value == 10)

print(result)

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
user_hours = input("Enter hours: ")
user_rate = input("Enter rate per hour: ")
earning = int(user_hours) * int(user_rate)
print("Your weekly earning is " + str(earning))

#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
user_year = input('Enter number of years you have lived: ')
calucate_seconds = 60 * 60 * 24 * 365 * int(user_year)
print("You have lived for " + str(calucate_seconds) + " seconds.")


#23 Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

## This table has 5 rows and 5 columns
num_rows = 5
num_columns = 5

## Loop through each row index
for i in range(1, num_rows + 1):
    # Need an empty list to store the current row's values
    row = []
    # Loop through each column index
    for j in range(1,num_columns):
        # Calculate i raised to the power of j and append to the row list
        row.append(i ** j)

    print(' '.join(map(str, row)))
