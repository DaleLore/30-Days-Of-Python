<!-- Day 11: 30 Days of python programming -->

# Exercises - Day 11
## Exercise Level 1
1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
6. Write a function called calculate_slope which return the slope of a linear equation
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
```
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
```

10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

```
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```

12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
```
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
```
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
```

14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

## Exercises - Level 2
1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
```
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```
2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

3. Call your function is_empty, it takes a parameter and it checks if it is empty or not

4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

## Exercises - Level 3
1. Write a function called is_prime, which checks if a number is prime.

2. Write a functions which checks if all items are unique in the list.

3. Write a function which checks if all the items of the list are of the same data type.

4. Write a function which check if provided variable is a valid python variable

5. Go to the data folder and access the countries-data.py file.
    - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
    - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

# Notes - Functions
- A function is a reusable block of code or programming statements designed to perform a certain task
- In object-oriented programming (like Java, Ruby, and C++ when used with classes), a function that belongs to a class is called a method.
- To define or declare a function, Python uses the keyword: <i>def</i>
- A function is executed only when it is called or invoked

## Declaring and Calling Functions
- When we create (make) a funciton, we're declaring it
- When we use a function, we are calling or invoking it
- The basic syntax of a function includes:
    - keyword <i>def</i>
    - name of function
    - Parentheses ()
        - Inside the parantheses we can have parameters;
        - Paramteres refer to a variable in a function definition that receives an argument (a value) when the function is called
        - They act as placeholders that allow a function to accept input values, which are then used within the function to perform a specific task.

```
# syntax
# Declaring a function
def function_name():
    codes
    codes

# Calling a function
function_name()
```

## Function Returning a Value 
- Functions can return values with the return keyword to send a result back to the caller and exit the function
    - To return a value with a function we use the keyword <i>return</i> followed by the variable we want returned
    - We can return any kindof data types types from a function
- If a function does not have a return statement, it will return None by default

```
# Example of a string
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

# Example of Boolean
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

## Functions with Parameters 
- We can pass different data types as a paramter (i.e. number, string, boolean, list, tuple, dictionary or set)
- If our function takes a parameter(s), we should call the function with an argument(s)
- The order of your arguments is important; if parameter_1 comes first followed by parameter_2, they must be passed in that order, or the arguments will be out of sequence.

```
# syntax for a single parameter
# Declaring a function
  def function_name(parameter):
    codes
    codes

# Calling function -- the argument is the parameter
  print(function_name(argument))


# syntax for two or more parameters
# Declaring a function
  def function_name(parameter_1, parameter_2)
    codes
    codes

# Calling function
  print(function_name(arg1, arg2))

```

## Functions without parameters
- You don't always need parameters
- Not all functions require external input to perform their tasks 
- Some functions might operate on: 
    - Global variables
    - Perform a specific action like printing a message
    - Carry out tasks that don’t depend on any input values

```
def greet():
    print("Hello, world!")
```

## Functions with Default Parameters
- We can pass a default value in our parameter
- When invoked, if no argument was passed when calling the function, the default value will be used
```
# syntax
# Declaring a function
def function_name(param = default_value):
    codes
    codes
# Calling function
function_name()    # this will have the default_value
function_name(arg)  
```

## Function as a Parameter of Another Function
- You can pass functions as arguments to other functions.

```
def square_number (n):
    return n * n

def pass_the_function(f, x):
    return f(x)

print(pass_the_function(square_number, 3))

```

## Passing Arguments with Key and Value
- If we pass the arguments with a key and value, the order of the arguments does not matter


## Arbitrary Number of Arguments
- If we do not know the number of argument we pass to the function, we can create a function whcih can take arbitrary number of arguments by adding * (asterik) before the parameter name

```
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)

# example
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

- You can have both default and an arbitrary number of parameters in functions
```
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)

print(generate_groups('Hashira','Sanemi','Giyu','Muichiro','Obanai'))
```

