# Day 1 - 30DaysOfPython Challenge
## To run this file in terminal, python3 hellowworld.py

# Exercise - Level 1
#1. Check the python version you are using
## python3 --version 

#2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
## Operations
print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 % 4)             # modulus(%)
print(3 // 4)            # Floor division operator(//)

#3. Write strings on the python interactive shell. The strings are the following:
## Your name
## Your family name
## Your country
## I am enjoying 30 days of python
## Write strings (in the python interactive shell)
print("Hello World")

#4. Check the data types of the following data:
## Checking data types
print(type(10))                                 # Int
print(type(9.8))                                # Float
print(type(3.14))                               # Float
print(type(4-4j))                               # Complex
print(type(['Asabeneh', 'Python', 'Finland']))  # List
print(type({'name':'Lore'}))                    # Dictionary

# Exercise - Level 2
##1. Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

# Exercise - Level 3
## 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
### Number: Integer 
print(type(10)) 

### Number: Float
print(type(9.8))   

### Number: Complex
print(type(4-4j))  

### String 
print(type('String'))  

### Boolean 
print(type(True))  

### List 
print(type(['Demon Slayer', 'Tanijro', 'Muzan']))

### Tuple 
print(type(('Demon Slayer', 'Tanijro', 'Muzan')))

### Set
print(type({9.8, 3.14, 2.7})) 

### Dictionary
print(type({'name':'Lore'}))   

##2.  Euclidian distance between (2, 3) and (10, 8)
### Need math module to use the square root function
import math

### Define the coordinates of the first point (p1) as a list.
p1 = [2, 3]

### Define the coordinates of the second point (p2) as a list.
p2 = [10, 8]

### The formula computes the Euclidean distance in a 2D space.
distance = math.sqrt((10-2)**2 + (8-3)**2)
print(distance)
