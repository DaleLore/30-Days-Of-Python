<!-- Day 17: 30 Days of python programming -->

# Exercises - Day 17

# Notes - Exception Handling
- Python uses <i>try</i> and <i>except</i> to handle errors gracefully
- A graceful exit (or graceful handling) of errors is a simple programming idiom where a program detects a serious error condition and "exits gracefully" in a controlled manner as a result
- Often the program prints a desceiption error message to a terminal or log as part of the graceful exit, this makes our application more robust
- The cause of an exception is often external to the program itself
- An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunction IO device
- Graceful handling of errors prevents our applications from crashing

- We have covered the different Python error types before and if we use try/except in our program, then it will not raise errors in those blocks
```
TRY > RUN THIS CODE _
                     |
EXCEPT (may or may not have a condition)
                     |
       EXECUTE THIS CODE WHEN THERE IS AN EXCEPTION
                     |
ELSE > No exceptions? Run this code
                     |
FINALLY > ALWAYS RUN THIS CODE
```

```
#syntax
try:
    code in this block if things go well
except:
    code in this block run if things go wrong

#example
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:') # This is a string
    age = 2019 - year_born # This is expecting a number - TypeError
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```

## Packing and Unpacking Arguments in Pythnon
- We use two operators
    -  *for tuples
    - ** for dictionaries

### Unpacking 
#### Unpacking Lists
- Unpacking lists in Python refers to the process of assigning the elements of a list (or any other iterable like tuples, sets, etc) to multiple variables in a single statement
- This is a useful feature for simplifying code when working with collections of values
- You can unpack with different lengths, with nested lists, and even lists in functions
    - Basic unpacking: assigns each element of a list to individual variables
    - Extended unpacking (*): Captures remaining elements when there are too many to unpack
    - Nested Unpacking: works with nested lists or other structures
    - Using in functions: The * operator can unpack a list into individual function arguments


```
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) 
# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# This function takes numbers (not a list) as arguments. You can unpack/destructure the list

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

#### Unpacking Tuples
- Unpacking tuples is similar to unpacking a list; it involves assigning the elements of a tuple to individual variables in a single statement
- Since tuples are immutable sequences (unlike lists), they are often used for fixed collections of items, making unpacking especially useful when working with tuples
- Similar to lists, you can unpack with different lengths, with nested lists, and even lists in functions; you can also use * for arbitary argument lists in functions
```
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Unpacking Dictionaries
- Unpacking dictionaries refers to extracting key-value pairs from a dictionary and using them in other contexts, such as passing them as arguments to a function or combining multiple dictionaries
- Python provides `**` operator to unpack dictionaries
```
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

person = {"name": "Alice", "age": 30}

# Unpacking dictionary
greet(**person)
# Output: Hello, Alice! You are 30 years old.
```

### Packing 
- Sometimes we never know how many arugments need to be passed to a Python function
- We can use the packing method to allow our functions to take unlimited number or arbitrary number of arguments

#### Packing Lists
- Packing refers to the process of grouping multiple values into a single variable, often as a lsit or tuple
- You can "pack" values into a list using square brackets by assigning multiple elements to a single variable
- This is commonly done when you're unsure of how many values need to be stored, or when you want to create a collection of elements to be handled as one object

```
# Packing multiple values into a list
my_list = [1, 2, 3, 4, 5]

print(my_list)
# Output: [1, 2, 3, 4, 5]
```

#### Packing Dictionaries
- Packing dictionaries refers to collecting multiple keyword arguments into a single dictionary
- This is commonly done using `**kwargs` in function definitions
- The process allows you to pass an arbitrary number of keyword arguments to a function, which Python then "packs" into a dictionary

```
def pack_kwargs(**kwargs):
    print(kwargs)

# Passing multiple keyword arguments
pack_kwargs(name="Alice", age=30, city="New York")
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### Spreading in Python
- Like in JavaScript, spreadking is possible Python where the concept is similar to unpacking sequences or collections and spreading their elements into different contexts
- This can be achieved using the `*` (for lists or tuples) and `**` (for dictionaries) operators
- These operators allow you to "spread" the elements of a collection when passing arguments to a function or when combining multiple collections

```
def sum_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# Using * to spread the list elements into function arguments
result = sum_numbers(*numbers)
print(result)
# Output: 6
```

### Enumerate
- If we are interested in an index of a list, we use<i>enumerate()</i>, a built-in function that allows us to loop over an iterable (such as a list, tuple, or string) and get both the index and the corresponding item in each iteration
- It returns an  `enumerate` object, which yields pairs containing the index and the item
- You can enumerate over lists, numbers, strings, etc

```
enumerate(iterable, start=0)
# iterable: The sequence you want to iterate over (e.g., a list, tuple, string).
# start: Optional parameter that defines the starting index (default is 0).

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### Zip
- Sometimes we would like to combine lists when looping through them
- This is when we use `zip()`, a built-in function that combines two or more iterables (e.g. lists, tuples) into a single iterator of tuples
- Each tuple contains elements from the input iterables at the same position and then stops when the shortest input iterable is exhausted so you can still zip iterables of different lengths
- Zip will take two or more iterables and combine them into tuples, one for each matching index across the iterables
    - The resulting iterator can eb converted to a list, tuple, or other iterable types


```
zip(*iterables)
# iterables: Any number of iterables (lists, tuples, strings, etc.).

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))
```