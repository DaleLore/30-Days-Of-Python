<!-- Day 15: 30 Days of python programming -->

# Exercises - Day 15
1. Open you python interactive shell and try all the examples covered in this section.

# Notes - Python Type Errors
- When our code fails to run due to an error, the Python interpreter will display a message containing feedback with information on where the problem occurs and the type of error
- If we're lucky, it will also sometimes give us suggestions on a possible fix
- Understanding different types of errors in programming langauges will help us to debug our code quickly

## SyntaxError
- SyntaxErrors occur when the interpreter encounters code that is not valid according to the Python languages rules or syntax

    -  Missing or Incorrect Punctuation:
        - Forgetting colons (:) after defining functions, loops, or conditionals
    ```
    def greet()
        print("Hello")
    # SyntaxError: Missing colon (:) after function definition
    ```

    -  Incorrect Indentation
        - Python relies on indentation to define blocks of code, and inconsistent indentation will result in a SyntaxError
    ```
    def greet():
        print("Hello")
    print("World")
    # SyntaxError: Unexpected indent or inconsistent indentation
    ```
    
    -  Mismatched Parentheses, Brackets, or Quotes
        - Forgetting to close a paranthesis, bracket, or string literal
    ```
    print("Hello world
    # SyntaxError: EOL (End of Line) while scanning string literal
    ```
    -  Invalid Variable or Function Names
        - Using invalid or reserved keywords as variable or function names
    ```
    class = 5
    # SyntaxError: 'class' is a reserved keyword in Python
    ```
    - Using Incomplete Statements
        - Not completing a multi-line statement properly
    ```
    if 5 > 3
    print("Hello")
    # SyntaxError: Missing colon or incomplete statement
    ```

## NameError
- A NameError occurs when the interpreter encounters a variable or function name that is not defined or accesible in the current scope
- This typically happenes when you try to use a vairable or funciton before declaring it, or if there's a typo in the name

    - Using an undefined variable
        - Referring to a variable that hasn't been initialized or declared
        ```
        print(x)
        # NameError: name 'x' is not defined
        ```

    - Typo in variable or function names
        - Misspelling a viarble or function name
        ```
        my_variable = 10
        print(my_varible)
        # NameError: name 'my_varible' is not defined
        ```
    
    - Using a variable outside of its scope
        - Trying to access a variable that is not in the current scope (e.g., referencing a local variable outside of its function).
        ```
        def my_function():
        x = 5

        print(x)
        # NameError: name 'x' is not defined (x is local to `my_function`)
        ```
## IndexError
- IndexError happens when you try to access an index that is out of range for a list, tuple, or other ordered lists
- This means that the index you are trying to access does not exist within the given sequence
    - Accessing an index that is too large
        - Trying to access an element at an index greater than or equal to the length of the list
        ```
        my_list = [1, 2, 3]
        print(my_list[5])
        # IndexError: list index out of range
        ```
    
    - Accessing a negative index that is out of bounds
        - Python allows negative indexing, but if the negative index is out of the range of the sequence, it will raise an IndexError
        ```
        my_list = [10, 20, 30]
        print(my_list[-4])
        # IndexError: list index out of range (valid negative indices are -1, -2, -3)
        ```
    
    - Empty sequences
        - Trying to access any index in an empty sequence will raise an IndexError
        ```
        empty_list = []
        print(empty_list[0])
        # IndexError: list index out of range
        ```

## ModuleNotFoundError
- A ModuleNotFoundError occues when the interpreter is unable to locate the module you are trying to import
    - Missing installation of a third-party module
        - If you try to import a third-party module that isn't installed in your environment, you'll get this error
        ```
        import numpy
        # ModuleNotFoundError: No module named 'numpy'

        # The fix is usually installing the module via a package manager like `pip`
        ```
    - Typo in the module name
        - If there's a mistake in the module name, Python will be unable to find it
        ```
        import numppy  # Typo in 'numpy'
        # ModuleNotFoundError: No module named 'numppy'
        ```
    
    - Inccorect module path
        - If you are trying to import a module from a specific directory or package, and the path is incorrect

## AttributeError
- An AttributeError occurs when you try to access or assign an attribute (method or variable) that does not exist for the object or data type you are working with
    - Accessing a non-existent attribute
        - Trying to call an attribute or method that is not defined for the object
        ```
        my_list = [1, 2, 3]
        my_list.append(4)
        print(my_list.size())  # 'size()' is not a method of list objects
        # AttributeError: 'list' object has no attribute 'size'
        ```

    - Typo in the attribute name
        - If you mistype the name of an attribute, Python will not recognize it, resulting in an AttributeError.
        ```
        my_string = "Hello"
        print(my_string.upperr())  # Typo in 'upper'
        # AttributeError: 'str' object has no attribute 'upperr'
        ```

    - Wrong object type
        - Trying to access an attribute that exists in one object type, but not in another.
        ```
        my_int = 10
        my_int.append(5)  # 'append()' is a list method, not an int method
        # AttributeError: 'int' object has no attribute 'append'
        ```
    
    - Accessing attributes before initialization
        - Trying to use an attribute that hasn't been defined yet
        ```
        class Car:
        def __init__(self, make):
            self.make = make

        my_car = Car('Toyota')
        print(my_car.model)  # 'model' was not defined in the class
        # AttributeError: 'Car' object has no attribute 'model'
        ```

## KeyError
- A KeyError occurs when you try to access a key in a dctionary that does not exist
    - Accessing a non-existenet key in a dictionary
        - Trying to retrieve a value from a dictionary using a key that does not exist
        ```
        my_dict = {"name": "Alice", "age": 25}
        print(my_dict["gender"])  # 'gender' key is not in the dictionary
        # KeyError: 'gender'
        ```
    
    - Case sensitivity
        - Dictionary keys are case-sensitive so using the wrong case will result in a KeyError
        ```
        my_dict = {"Name": "Alice", "Age": 25}
        print(my_dict["name"])  # 'name' is not the same as 'Name'
        # KeyError: 'name'
        ```

    - Using a key that is not in the dictionary
        - If a key is amissing in the dictionary, you will get a KeyError
        ```
        user_data = {"username": "john_doe", "email": "john@example.com"}
        print(user_data["phone"])  # No 'phone' key in the dictionary
        # KeyError: 'phone'
        ```
## TypeError
- This occues when an operation or function is applied to an object of an inappropriate type; so when you try to perform an operation that is not allowed for a specific data type
    
    - Using incompatible types in operations:
        - Trying to perform operations between incompatible data types (e.g., adding a string to an integer).
        ```
        result = "hello" + 5
        # TypeError: can only concatenate str (not "int") to str
        ```

    - Calling a function with the wrong number of arguments
        - Passing the wrong number or type of arguments to a function
        ```
        def add(a, b):
            return a + b

        add(5)  # Missing the second argument
        # TypeError: add() missing 1 required positional argument: 'b'
        ```
    
    - Using a method or operation that is not supported by the data type
        - Trying to call a method or operation that is invalid for that type
        ```
        my_list = [1, 2, 3]
        my_list.upper()
        # TypeError: 'list' object has no attribute 'upper'
        ```
    - Wrong data type for indexing or slicing
        - Using a non-integer type of indexing
        ```
        my_list = [1, 2, 3]
        print(my_list["0"])  # Indexing with a string instead of an integer
        # TypeError: list indices must be integers or slices, not str
        ```

## ImportError
- This occurs when the interpreter fails to import a module or a specific object (e.g. function, class) from a module

    - Missing module
        - The module you're trying to import is not installed
        ```
        import pandas
        # ImportError: No module named 'pandas'
        ```

    - Incorrect module name or path
        - There's a typo in the module name, or you're trying to import a module from a wrong location
        ```
        from math import squareroot  # Typo, should be 'sqrt'
        # ImportError: cannot import name 'squareroot' from 'math'
        ```

    - Circular Imports
        - Two or more modules depend on each other, creating a circular import
        ```
        # file1.py
        from file2 import func2

        # file2.py
        from file1 import func1
        # ImportError: cannot import name 'func1'
        ```

    - Invalid module structure
        - You're trying to import something that isn't properly set up or doesn't exist in the module
        ```
        from math import non_existent_function
        # ImportError: cannot import name 'non_existent_function' from 'math'
        ```

    - Problems with the Python environment
        - The module migth be installed in another environment or virtual environment, and you're not using the correct one
    
    - NOTE: What is the different between `ImportError` and `ModuleNotFoundError`?
        - ImportError is a broader error that can occur for various reasons related to importing a module or object.
        - ModuleNotFoundError is a subclass of ImportError and specifically occurs when a module cannot be found.
 
## ValueError
- This occurs when a function receives an argument of the correct type but with an inappropriate or invalid value so when the data you are working with is the right type, but its value doesn’t meet the function’s requirements.

    - Invalid literal for a type conversion:
        - Trying to convert a string that doesn’t represent a valid number into an integer or float.
        ```
        int("hello")
        # ValueError: invalid literal for int() with base 10: 'hello'
        ```

    - Invalid argument for a function
        - Passing a value that doesn't fit  the function's expectations 
        ```
        import math
        math.sqrt(-1)  # Square root of a negative number is not allowed
        # ValueError: math domain error
        ```

    - Improper input format
        - When a value doesn’t conform to the expected format for a function or operation
        ```
        from datetime import datetime
        datetime.strptime("32/01/2024", "%d/%m/%Y")  # Day '32' is invalid
        # ValueError: time data '32/01/2024' does not match format '%d/%m/%Y'
        ```

    - Unpacking mismatched number of values
        - Trying to unpack more or fewer values than the iterable holds
        ```
        a, b = [1, 2, 3]  # Trying to unpack 3 values into 2 variables
        # ValueError: too many values to unpack (expected 2)
        ```

## ZeroDivisionError
- A ZeroDivisionError in Python occurs when a number is divided by zero, which is mathematically undefined. This error is raised when either an integer or a float is divided by zero using division (/) or floor division (//) operations.
     - Division by zero in integer or float division:
        - Attempting to divide a number by zero using the division operator (/).
    ```
    result = 10 / 0
    # ZeroDivisionError: division by zero
    ```

    - Division by zero in floor division:
        - Using floor division (//) with zero as the divisor.
    ```
    result = 10 // 0
    # ZeroDivisionError: integer division or modulo by zero
    ```

    - Modulo operation with zero
        - Using the modulo operator (%) with zero as the divisor.
    ```
    numerator = 5
    denominator = 0
    result = numerator / denominator
    # ZeroDivisionError: division by zero
    ```
