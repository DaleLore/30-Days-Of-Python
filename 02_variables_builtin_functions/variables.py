# Day 2: 30 Days of Python

## Exercises: Level 1
### Declare a first name variable and assign a value to it
first_name = 'James'

### Declare a last name variable and assign a value to it
last_name = 'Bond'

### Declare a full name variable and assign a value to it
full_name = 'James Bond'

### Declare a country variable and assign a value to it
country = 'England'

### Declare a city variable and assign a value to it
city = 'London'

### Declare an age variable and assign a value to it
age = 37

### Declare a year variable and assign a value to it
year = 2024

### Declare a variable is_married and assign a value to it
is_married = False 

### Declare a variable is_true and assign a value to it
is_true = True 

### Declare a variable is_light_on and assign a value to it
is_light_on = True 

### Declare multiple variable on one line
agent, assignment, licensed_to_kill = 7, "Helsinki", True

## Exercises: Level 2

### Check the data type of all your variables using type() built-in function
type(agent)

### Using the len() built-in function, find the length of your first name
len(first_name)

### Compare the length of your first name and your last name
first_name==last_name

### Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#### Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#### Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
#### Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
#### Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#### Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#### Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#### Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

### The radius of a circle is 30 meters

#### Calculate the area of a circle and assign the value to a variable name of area_of_circle

#### pi * r squared
area_of_circle = 3.14 * 30 ** 2
#### Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * 30
#### Take radius as user input and calculate the area.
radius = input('Enter radius: ')
area = 3.14 * int(radius) ** 2
print(area)


### Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
input()

### Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
#### In python shell
help('keywords')