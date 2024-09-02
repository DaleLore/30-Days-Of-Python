# Day 1 - 30DaysOfPython Challenge
## To run this file in terminal, python3 hellowworld.py

## Operations
print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 % 4)             # modulus(%)
print(3 // 4)            # Floor division operator(//)

## Write strings (in the python interactive shell)
print("Hello World")

## Checking data types
print(type(10))                                 # Int
print(type(9.8))                                # Float
print(type(3.14))                               # Float
print(type(4-4j))                               # Complex
print(type(['Asabeneh', 'Python', 'Finland']))  # List
print(type({'name':'Lore'}))                    # Dictionary

##  Euclidian distance
### Need math module to use the square root function
import math

### Define the coordinates of the first point (p1) as a list.
p1 = [2, 3]

### Define the coordinates of the second point (p2) as a list.
p2 = [10, 8]

### The formula computes the Euclidean distance in a 2D space.
distance = math.sqrt((10-2)**2 + (8-3)**2)
print(distance)
