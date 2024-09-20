<!-- Day 19: 30 Days of python programming -->

# Exercises - Day 19
## Exercises - Level 1
1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
```
# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
```

3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
```
# Your output should look like this
print(most_populated_countries(filename='./data/countries_data.json', 10))

[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]

# Your output should look like this

print(most_populated_countries(filename='./data/countries_data.json', 3))
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]
```
## Exercises - Level 2
1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.

2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output:
```
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```
3. Use the function, find_most_frequent_words to find:
    - The ten most frequent words used in Obama's speech
    - The ten most frequent words used in Michelle's speech
    - The ten most frequent words used in Trump's speech
    - The ten most frequent words used in Melina's speech

4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

5. Find the 10 most repeated words in the romeo_and_juliet.txt

6. Read the hacker news csv file and find out:
    - Count the number of lines containing python or Python 
    - Count the number lines containing JavaScript, javascript or Javascript 
    - Count the number lines containing Java and not JavaScript

# Notes - File Handling
- File handling is an import part of programming which allows us to create, read, update, and delete files
- An important built-in function to handle data is `open()`

    - Opening Files for Reading
        - Syntax: open('filename', mode)
        - Mode options
            - `r` - Read - default value - this opens a file for reading, it returns an error if the file does not exist
            - `a` - Append - opens a file for appending, creates the file if it does not exist
            - `w` - Write - Opens a file for writing, creates the file if it does not exist
            - `x` - Create - Creates the specified file, returns an error if the file exists
            - `t` - Text - Default value - text mode
            - `b` - Binary - binary mode (e.g. images)
    
    - Opening Files for Writing and Updating
        - The default mode of open is reading so adding `r` isn't necessary a lot of the times

    - Deleting Files

- File Types
    - File with txt extension
    - File with json Extension
    - Changing JSON to dictionary
    - Changing Dictionary to JSON
    - Saving as JSON file
    - File with CSV Extension
    - File with XLSX Extension
    - File with XML Extension

