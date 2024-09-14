<!-- Day 13: 30 Days of python programming -->

# Exercises - Day 13
1. Filter only negative and zero in the list using list comprehension
```
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
```

2. Flatten the following list of lists of lists to a one dimensional list :
```
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

3. Using list comprehension create the following list of tuples:
```
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
```

4. Flatten the following list to a new list:
```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
```

5. Change the following list to a list of dictionaries:
```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
```

6. Change the following list of lists to a list of concatenated strings:
```
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
```

7. Write a lambda function which can solve a slope or y-intercept of linear functions.


# Notes - List Comprehension
- List comprehension is a compacy way of creating a list from a sequence
    - It's a shorter way to create a new list; it faster than processing a list using the <i>for</i> loop

```
# syntax 
[i for i in iterable if expression]

# Example 1
language = 'Python'
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Example 2
numbers = [i for i in range(11)]
print(numbers)

# Example 3
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)
```

## Lambda Function
- The lambda function is a small anonymous function without a name
- It can take any number of arguments, but can only have one expression
- Lambda functions are similar to anonymous functions in JavaScript

- Creating a lambda function requires the keyword <i>lambda</i> followed by a parameter(s), then followed by an expression
```
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))

# Example
def add_two_nums(a, b):
    return a + b

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5
```

- You can use lambda functions inside another function by defining the lambda within the body of the outer function; Lambda functions are anonymous, inline functions that are often used for small, quick operations.