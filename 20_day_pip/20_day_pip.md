<!-- Day 20: 30 Days of python programming -->

# Exercises - Day 20
## Exercises 

# Notes - PIP
- PIP stands for Preferred Installer Program
- We use `pip` to install different Python packages
    - A package is a Python module that can contain one or more modules or other packages in it
    - A module or modules that we can install to our application is a package
- Fortunately in programming, we do not have to write every utility program, instead we install packages and import them to our applications

## Installing PIP
```
# Check if you have pip installed
pip --version
```

- If pip is not installed, go to the [pip documentation](https://pip.pypa.io/en/stable/installation/) to download and install
    - Download the script, from https://bootstrap.pypa.io/get-pip.py
    ```
    curl https://bootstrap.pypa.io/get-pip.py | python
    OR
    curl https://bootstrap.pypa.io/get-pip.py | python3
    ```

## Installing packages using pip: NumPY
- Let's try to install <i>numpy</i>, numeric python; it's a popular package in machine learning and data science
    - NumPy is the fundamental package for scientific computing with Python because it contains things like: 
        - powerful N-dimensional array object
        - sophisticated (broadcasting) functions
        - tools for integrating C/C++ and Fortran code
        - useful linear algebra, Fourier transform, and random number capabilities

```
pip install numpy
```

## Installing packages using pip: Panadas
- Pandas is an open-source, BSD-licensed library used for data manipulation and analysis. It provides data structures and functions needed to work with structured data, making it easier to handle, analyze, and visualize data.

```
pip install pandas
```

## Uninstalling packages
- You can always remove a package using pip as well
```
pip uninstall packageName
```

## List of packages
- To see the installed packages on your machine, you can list them with pip
```
pip list
```

## Show Packages
- To show information about a package,  you can show packageName with pip
    - For more details, add the flag for verbose
```
pip show packageName
pip show --verbose packageName
```

## PIP Freeze
- Generate installed Python packages with their version and the output is suitable to use it in a requirements file
- A requirements.txt is a file that should contain all the installed Python packages in a Python project

```
pip freeze
package_01
package_02
package_03
```


