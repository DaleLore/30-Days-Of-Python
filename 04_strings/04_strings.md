<!-- Day 4: 30 Days of python programming -->

# Exercises - Day 4
- Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
- Declare a variable named company and assign it to an initial value "Coding For All".
- Print the variable company using print().
- Print the length of the company string using len() method and print().
- Change all the characters to uppercase letters using upper() method.
- Change all the characters to lowercase letters using lower() method.
- Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
- Cut(slice) out the first word of Coding For All string.
- Check if Coding For All string contains a word Coding using the method index, find or other methods.
- Replace the word coding in the string 'Coding For All' to Python.
- Change Python for Everyone to Python for All using the replace method or other methods.
- Split the string 'Coding For All' using space as the separator (split()) .
- "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
- What is the character at index 0 in the string Coding For All.
- What is the last index of the string Coding For All.
- What character is at index 10 in "Coding For All" string.
- Create an acronym or an abbreviation for the name 'Python For Everyone'.
- Create an acronym or an abbreviation for the name 'Coding For All'.
- Use index to determine the position of the first occurrence of C in Coding For All.
- Use index to determine the position of the first occurrence of F in Coding For All.
- Use rfind to determine the position of the last occurrence of l in Coding For All People.
- Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Does ''Coding For All' start with a substring Coding?
- Does 'Coding For All' end with a substring coding?
- '   Coding For All      '  , remove the left and right trailing spaces in the given string.
- Which one of the following variables return True when we use the method isidentifier():
    - 30DaysOfPython
    - thirty_days_of_python
- The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
- Use the new line escape sequence to separate the following sentences: I am enjoying this challenge. I just wonder what is next.
- Use a tab escape sequence to write the following lines: Name, Age, Country, City, Asabeneh, 250, Finland, Helsinki
- Use the string formatting method to display the following:
```
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```
- Make the following using string formatting methods
```
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

# Notes
## Strings
- A test is a string data type; any data type written as text is considered a string
- Any string in 'single', "double", or '''triple''' quotes are strings

### Create a string

```
single_quote = 'Python'

double_quote = "30 days of Python"

triple_multiline_string = '''During this challenge, I will be learning everything needed to be a python programmer and the whole concept of programming. In the end of the challenge, I will get a 30DaysOfPython programming challenge certificate.'''
```

### String concatenation
- Connect strings with +
```
first_word = "one"
second_word = "piece"
youll_learn_spacing_later = " "
anime = first_word + youll_learn_spacing_later + second_word
print(anime)
```

### Escape sequences in strings
- \n: new line
- \t: Tab means(8 spaces)
- \\: Back slash
- \': Single quote (')
- \": Double quote (")

### String Formatting
- Old Style (using % operator)
    - %s: String (or any object with a string representation, like numbers)
    - %d: Integers
    - %f: Floating point numbers
    - "%.number of digitsf": Floating point numbers with fixed precision

```
# Example of a string
anime = "One Piece"
formatted_string = 'Currently watching %s' %(anime)

# Example of strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
```
- New Style (str.format)
    - Introduced in Python version 3 so don't worry if you didn't remember using this before v3

```
# Example of a string
anime = "One Piece"
formatted_string = 'Still watching {}'.format(anime)

# Example of strings and numbers
radius = 100
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius {} is {:.2f}'.format(radius, area)
```

### String Interpolation / f-Strings
- Another new string formatting introduced in Python 3.6+ is string interpolations
- We can inject data in their positions with strings starting with f
```
x = 10
y = 13
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
```

### Python Strings as Sequences of Characters
- Python strings are sequences of characters
- These strings share basic methods of access with other Python ordered sequences like lists and tuples
- The simplest way of extracting single characters from strings (and invdiviual characters from any sequence) is to unpack them into corresponding variables

```
# Unpacking
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Indexing
language = 'Python'
first_letter = language[0]
print(first_letter) 
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) 

# Slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) 
last_three = language[3:6]
print(last_three) 
# Another way
last_three = language[-3:]
print(last_three)   
last_three = language[3:]
print(last_three)   

# Reversing
greeting = 'Hello, World!'
print(greeting[::-1]) 

# Skip / Slice
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

```

### Python String Methods
- There are many built-in string methods to format strings
    - capitalize()
    - count()
    - endswith()
    - expandtabs(): replaces tab character with spaces; the default tab size is 8
    - find(): returns the index of the first occurrence of a substring
    - rfind(): returns the index of the last occurence of a substring
    - format(): formats string into a nicer output
    - index(): returns the lowest index of a substring
    - rindex(): returns the highest index of a substring
    - isalnum(): checks alphanumeric character
    - isalpha(): checks if all the string elements are alphabet characters
    - isdecimal(): checks if all characters in a string are decimal (0-9)
    - isdigit(): checks if all characters in a string are numbers (0-9)
    - isnumeric(): checks if all characters in a string are numbers or number related
    - isidentifier(): checks for a valid identifier
    - islower(): checks if all alphabet characters in the string are lowercase
    - isupper(): checks if all alphabet characters in the string are uppercase
    - join(): returns a concatenated string
    - strip(): removes all given characters starting from the beginning and end of the string
    - replace(): replaces substring with a given string
    - split(): splits the string, using given string or space as a separator
    - title(): returns a title cased string
    - swapcase(): conversta all uppercase characters to lowercase and all lowercase characters to uppercase characters
    - startswith(): checks if string starts with the specified string