<!-- Day 14: 30 Days of python programming -->

# Exercises - Day 14
## Exercise Level 1
1. Explain the difference between map, filter, and reduce.

2. Explain the difference between higher order function, closure and decorator

3. Define a call function before map, filter or reduce, see examples.

4. Use for loop to print each country in the countries list.

5. Use for to print each name in the names list.

6. Use for to print each number in the numbers list.

## Exercise Level 2
1. Use map to create a new list by changing each country to uppercase in the countries list

2. Use map to create a new list by changing each number to its square in the numbers list

3. Use map to change each name to uppercase in the names list

4. Use filter to filter out countries containing 'land'.

5. Use filter to filter out countries having exactly six characters.

6. Use filter to filter out countries containing six letters and more in the country list.

7. Use filter to filter out countries starting with an 'E'

8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

10. Use reduce to sum all the numbers in the numbers list.

11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

## Exercise Level 3
1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
    - Sort countries by name, by capital, by population
    - Sort out the ten most spoken languages by location.
    - Sort out the ten most populated countries.

# Notes - Higher Order Functions
- Functions in Python are highly versatile and can be used for a variety of tasks, including:
    - A function can take one or more functions as parameters
    - A function can be returned as a result of another function
    - A function can be modified
    - A function can be assigned to a variable

## Function as a Parameter
- You can pass a function as a parameter (or argument) to another function;
- This allows you to make functions more flexible and reusable by passing different functions for different behaviors.

```
# This function takes another function (func) and a value (value) as parameters. It calls the passed function func with the given value

def apply_function(func, value):
    return func(value)

# Simple math functions
def square(x):
    return x * x

def cube(x):
    return x * x * x

# Passing Functions: When you call apply_function(square, 5), you are passing the square function as an argument, which is then called inside apply_function

print(result1)  # Output: 25
print(result2)  # Output: 27
```

## Function as a Return Value
- A function can return another function as a result
- It allows you to create higher-order functions, which can be useful for designing flexible, reusable, and modular code

```
# This function takes a parameter x and defines an inner function that adds x to y.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function # The outer_function returns the inner inner_function, not a specific result yet, but the function itself

# Example usage
add_five = outer_function(5)  # Returns a function that adds 5
result = add_five(10)         # Calls the returned function with 10
print(result) 
```

## Python Closures
- Closure is when python allows a nested function to access the outer scope of the enclosing function
- Closure is created by nesting a function inside another encapsulating function and then returning the inner funtion

```
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
```

## Python Decorators
- A decorator is a design pattern in Python that allows a user to add new funcitonality to an existing object without modifying its structure
- Decorators are usually called before the definition of a function  you want to decorate

- To create a decorator function, you need an outer function that contains an inner wrapper function.

## Applying Multiple Decorators to a Single Function

## Accepting Parameters in Decorator Functions

## Built-in Higher Order Functions