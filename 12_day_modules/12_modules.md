<!-- Day 12: 30 Days of python programming -->

# Exercises - Day 12
## Exercise Level 1
## Exercise Level 2
## Exercise Level 3

# Notes - Modules
- A module is a file containing a set of codes or a set of functions which can be imported and used in other Python programs
- A module can be as simple as a file with a single variable or function, or as complex as a large code base.
- Modules help organize and reuse code, making it more manageable and maintainable.

## What to do with Modules
- Creating a module follows the same steps as creating any Python script. The first step is simply saving it as a .py file.

- You can import the entire file with the keyword, <i>import</i>
```
import file_name
```

- You can import a specific function(s) with <i>import</i> as well
```
from file_name import function_1, function_2, funtion_3
```

- You may need to rename a function when importing it into a different context
```
from file_name import function_1 as method_1, function_2 as method_1, funtion_3 as method_1
```

## Import Built-In Modules
- Python comes with a large number of built-in modules, and the exact number can vary depending on the version and the specific Python distribution you're using, but you can see a general list on [w3schools Module Index for Python](https://docs.python.org/3/py-modindex.html) or in a filem write:
```
import sys
print(sys.builtin_module_names)
```

- The standard library includes hundreds of modules covering a wide range of functionalities, from file handling to mathematical operations and network communication
    - Example: datetime: Date and time manipulation.
    - Example: json: JSON data parsing and generation.
    - Example: collections: High-performance container datatypes.

### OS: Operating system interfaces
- This provides functions for creating, changing current working direcotry and removing a directory, fetching its contents, changing and identifying the current directory
```
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### SYS: System-specific parameters and functions
- This provides functions and variables used to manipulate different parts of the Python runtime environment.
- Function sys.argc returns a list of command line arguments passed to a Python script
- The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line
```
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

# In terminal
python script.py Python coder 30DaysOfPython
```

### Statistics
- This module provides functions for mathematical statistics of numeric data
- Some popular statistical functions are: mean, median, mode, stdev

### math: Mathematical functions
- This module contains many mathematical operations and constants
- This module can also help us to perform mathematical calculations. 
    - To check what functions the module has got, we can use help(math), or dir(math)

### String
- A string module provides various constants, utility functions, and classes to work with strings more efficiently. It includes pre-defined string constants like all letters or digits, and also provides templates for advanced string formatting.
```
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random: Random number generation.
- This module provides random numbers between 0 and 0.9999+
```
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```
  