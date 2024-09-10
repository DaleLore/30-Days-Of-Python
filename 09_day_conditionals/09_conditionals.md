<!-- Day 9: 30 Days of python programming -->

# Exercises - Day 9


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