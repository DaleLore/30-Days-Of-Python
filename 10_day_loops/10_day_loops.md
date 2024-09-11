<!-- Day 10: 30 Days of python programming -->

# Exercises - Day 10
## Exercise Level 1
## Exercise Level 2
## Exercise Level 3

# Notes - Loops
- A loop in Python is a programming construct that allows you to repeat a block of code multiple times, based on a condition. 
- There are two main types of loops in Python:  <b>for</b> loops and <b>while</b> loops.

## For Loops
- <i>for</i> is one of Python's reserved words
- A for loop can be used to iterate over a type of sequence like a list, tuple, set, or string

```
# syntax for a list
for iterator in lst:
    code goes here

# syntax for a string
for iterator in string:
    code goes here

# syntax for a tuple 
for iterator in tpl:
    code goes here

# syntax for a set
for iterator in st:
    code goes here

# syntax for a dictionary
## NOTE: Looping through a dictionary will give you the key 
for iterator in dct:
    code goes here
```

## While Loops
- <i>while</i> is another one of Python's reserved words
- It is used to execute a block of code repeatedly until a given condition is met
- When the condition becomes false, the code will continue to loop

```
# syntax
while condition:
    code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1

# the condition becomes false when count is 5. That is when the loop stops
```

- If we want to execute a block of code after the condition becomes false, we can use <i>else</i>. 

```
# syntax
while condition:
    code goes here
else:
    code goes here

# example
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. In the end, 5 will be printed
```

## Break and Continue
- Break is used when we need to get out of or stop either a for or while loop

```
# syntax for a while loop
while condition:
    code goes here
    if another_condition:
        break

# Example for a while loop
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

## The while loop will continue ubtil 3 is reached

# syntax for a for loop
for iterator in sequence:
    code goes here
    if condition:
        break 

# Example for a for loop
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

- Continue is used when we want to skip a current iteration, and continue with the next line of code

```
# syntax for a while loop
while condition:
    code goes here
    if another_condition:
        continue

# Example for a while loop
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

## The above while loop only prints 0, 1, 2 and 4 (skips 3)

# syntax for a for loop
for iterator in sequence:
    code goes here
    if condition:
        continue

# example for a for loop
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

## If the number equals 3, the step following the condition (but still within the loop) is skipped, and the loop continues with any remaining iterations.
```

## Range Function
- The <i>range</i> function is used to list numbers
- The <i>range</i> function takes three parameters
    - Start of te sequence; by default it starts from 0
    - End of the sequence
    - Increments (step); by default the increment is 1

```
# syntax
range(start, end, step)

# example
lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

## Nested For Loop
- Remember that we can write loops inside of loops

```
# syntax
for x in y:
    for t in x:
        print(t)
```

## For Else
- Similar to for else statements, we can execute a message when the loops ends with else

```
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')

```

## Pass
- In Python, when a statement is required (after a semilcolon), but we don't want to execute any code, we can write the word <i>pass</i> to avoid errors
```
for number in range(6):
    pass
```