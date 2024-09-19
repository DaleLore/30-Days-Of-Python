<!-- Day 18: 30 Days of python programming -->

# Exercises - Day 18
## Exercises - Level 1
1. What is the most frequent word in the following paragraph?
```
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

```
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
```

## Exercises - Level 2
1. Write a pattern which identifies if a string is a valid python variable
```
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
```

## Exercises - Level 3
1. Clean the following text. After cleaning, count three most frequent words in the string.

```
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
```

# Notes - Regular Expressions
- A regular expression (or RegEx) is a special text string that helps to find patterns in data
- A RegEx can be used to check if some pattern exists in a different data type
- To use RegEx in Python, we first need to impor the RegEx module, called `re`

```
import re
```

- There are methods in the re module used for different purposes
    - re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None
    ```
    # syntax
    import re

    result = re.match(pattern, string)
    # pattern refers to the regex pattern you want to search for
    # string is what you are tryiing to match the pattern

    # example
    # Define a pattern and a string
    pattern = r"hello"
    r indicate raw string literal
    string = "hello world"

    # Use re.match() to check if the pattern matches the start of the string
    match = re.match(pattern, string)

    if match:
        print("Pattern found!")
    else:
        print("Pattern not found.")
    ```
    
    - re.search: returns a match object if there is one anywhere in the string, including multiline strings
    ```
    # syntax
    import re

    result = re.search(pattern, string)

    # Define a pattern and a string
        pattern = r"\d+"  
        # `\d+` Matches one or more digits

        string = "My house number is 1234"

    # Use re.search() to find the first occurrence of the pattern
        match = re.search(pattern, string)

    if match:
        print("Match found:", match.group())  
        # .group returns the matched portion of the string - Output: Match found: 1234
    else:
        print("No match found")
    ```

    - re.findall: returns a list containing ALL matches
    ```
    # syntax
    import re

    result = re.findall(pattern, string)

    # Define a pattern and a string
        pattern = r"\d+"  # Matches one or more digits
        string = "There are 123 apples and 456 bananas."

    # Use re.findall() to find all occurrences of the pattern
        matches = re.findall(pattern, string)

    print("Matches:", matches)  # Output: ['123', '456']
    ```
    - re.sub: replaces one or many matches within a string
    ```
    # syntax
    import re

    result = re.sub(pattern, replacement, string, count=0, flags=0)
        # pattern is the regular expression pattern to search for
        # replacement is the string that will replace the matched pattern
        # string is where the pattern will be search and replaced
        # count (optional) is for the maximum number of replacements to make; by default its 0
        # flags (optional) is used to modify the behavior of the pattern matchings, such a re.IGNORECASE
    
    # example 
        # Replace all digits in the string with '#'
        pattern = r"\d"  # Matches any digit
        replacement = "#"
        string = "Phone: 123-456-7890"

        result = re.sub(pattern, replacement, string)

        print(result)  # Output: Phone: ###-###-####
    ```

    - re.split: takes a string, splits it at the match points, returns a list
    ```
    # syntax
    import re

    result = re.split(pattern, string, maxsplit=0, flags=0)
        # pattern is the regular expression pattern to split by
        # string is the string to be split
        # maxsplit (optional) is the maximum number of splits; by default it's 0 so no limit
        # flags (optional) is to modify the pattern's behaviour, such as re.IGNORECASE

    # example
        # Split the string by one or more spaces
        pattern = r"\s+"
        string = "Split  this  string by  spaces."

        result = re.split(pattern, string)

        print(result)  # Output: ['Split', 'this', 'string', 'by', 'spaces.']
    ```

## Writing RegEx Patterns
- To declare a string variable we use a single or double quote
- To declare RegEx varioable r''
    - Square Bracket
        - Example: [a-z] means, any letter from a to z

    - Escape character (\) in RegEx
        - Example: \d means: match where the string contains digits (numbers from 0-9)

    - One or moret times (+)
        - Example: r'[a]+' means at least once (or more)

    - Period(.)
        - any character except new line character(\n)
        - Example: 

    - Zero or more times (*)
        - Example: r'[a]*' means a optional or it can occur many times.

    - Zero or one time (?)
        - Example: r'[a]?' means zero times or once

    - Quantifier in RegEx
        - Example: 

    - Cart ^
        - Example: r'[^abc] means not a, not b, not c.
    
    - $: ends with
        - Example: r'substring$' eg r'love$', sentence that ends with a word love

    - |: Either or
        - Example: r'apple|banana' means either apple or a banana

    - (): Capture and group

