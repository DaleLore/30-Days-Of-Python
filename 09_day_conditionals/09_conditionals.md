<!-- Day 9: 30 Days of python programming -->

# Exercises - Day 9
## Exercise Level 1
1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
```
# Output
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
```

2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

```
# Output
Enter your age: 30
You are 5 years older than me.
```

3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

```
# Output
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

## Exercise Level 2

4. Write a code which gives grade to students according to theirs scores:

```
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

```

5. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

6. The following list contains some fruits: fruits = ['banana', 'orange', 'mango', 'lemon']
    - If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

## Exercise Level 3
7. Modify this person dictionary: 
    * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
    * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
    * If the person is married and if he lives in Finland, print the information in the following format:

```
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```


# Notes - Conditionals
- By default, statements in Python are executed sequentially from top to bottom
- The sequential flow of execution can be altered in two ways:
    - Through a conditional execution where a block of one or more statements will be excuted if a certain expression is true;
    - Or through a repetitive execution where a block of one or more statements will be repetitively executed as long as a certain expression is true

## If Condition
- Using the <i>if</i> condition checks if a condition is true and to execute the block code 
    - REMEMBER THE INDENTATION AFTER THE COLON
```
#syntax 
if condition
    this part of the code runs for truthy conditions

# example
a = 3

if a > 0:
    print("A is greater than 0")
```

## If Else
- If-else statements combine the use of the <i>if</i> condition with <i>else</i>. 
- If the condition is true, the first block will execute; otherwise, the <i>else</i> block will run.
```
#syntax 
if condition
    this part of the code runs for truthy conditions
else:
    this part of the code for false conditions

# example
a = 3

if a > 0:
    print("A is greater than 0")
else:
    print("A is not greater than 0")
```

## If elif else
- The <elif> statement is when we have multiple conditions
```
#syntax 
if condition
    code
elif condition:
    code
else:
    code

# example
a = 3

if a > 0:
    print("A is greater than 0")
elsif a < 0:
    print("A is not greater than 0")
else:
    print("A is zero")
```

## Short Hand
- You can simplify if-else statements into a single line of code.
``` 
# syntax 
code if condition else code

# example
print('A is positive') if a > 0 else print('A is negative')
```

## Nested Conditions
- You can have <i>if</i> conditions INSIDE <i>if</i> conditions

```
# syntax
if condition:
    code
    if condition:
    code

# example
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

## If Condition and Logical Operators
- Generally you can avoid writing nested conditions by using the logical operator <i>and</i>
- Returns True if both conditions are true
```
# syntax
if condition and condition:
    code

# example
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

## If and Or Logical Operators
- Similar to If / And Operators, If / Or will avoid nested conditions
- Returns True if at least one condition is true
```
# syntax
if condition or condition:
    code

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```