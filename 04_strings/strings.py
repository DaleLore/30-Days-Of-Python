#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_01 = "Thirty"
word_02 = "Days"
word_03 = "Of"
word_04 = "Python"
space = " "
single_string = word_01 + space + word_02 + space + word_03 + space + word_04
print(single_string)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_01 = "Coding"
word_02 = "For"
word_03 = "All"
single_string = word_01 + space + word_02 + space + word_03
print(single_string)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
company_length = len(company)
print(company_length)

#6 Change all the characters to uppercase letters using upper() method.
uppercase_company = company.upper()
print(uppercase_company)

#7 Change all the characters to lowercase letters using lower() method.
lowercase_company = company.lower()
print(lowercase_company)

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
sliced_word = company[7:]
print(sliced_word)

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
## Index Method
sub_string = "Coding"
print(company.index(sub_string))

## Find Method
print(company.find(sub_string))

#11 Replace the word coding in the string 'Coding For All' to Python.
replace_coding = company.replace('Coding', 'Python')
print(replace_coding)

#12 Change Python for Everyone to Python for All using the replace method or other methods.
# Note: it might be change Python for All to Python for Everyone
print(replace_coding.replace('All', 'Everyone'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
split_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(split_string.split(','))

#15 What is the character at index 0 in the string Coding For All.
print(company[0])

#16 What is the last index of the string Coding For All.
print(company[-1])

#17 What character is at index 10 in "Coding For All" string.
print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
acronym = ''.join(word[0] for word in string.split())
print(acronym)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
string_02 = "Coding For All"
acronym_02 = ''.join(word[0] for word in string_02.split())
print(acronym_02)

#20 Use index to determine the position of the first occurrence of C in Coding For All.
string = "Coding For All"
first_c = 'C'
print(string_02.index(first_c))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
string = "Coding For All"
first_f = 'F'
print(string_02.index(first_f))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = "Coding For All People"
last_l = 'l'
print(string.rindex(last_l))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
long_sentence = 'You cannot end a sentence with because because because is a conjunction'
split_long_sentence = long_sentence.split()
print(split_long_sentence.index('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
long_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(long_sentence.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
long_sentence = 'You cannot end a sentence with because because because is a conjunction'

start = long_sentence.index('because because because')
end = start + len('because because because')

print(start)
print(end)
sliced_sentence = long_sentence[:start] + long_sentence[end:]
print(sliced_sentence)

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## RE: I think this is the same Task 23(⊙.☉)7 

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## RE: I think this is the same as Task 25 ¿ⓧ_ⓧﮌ

#28 Does ''Coding For All' start with a substring Coding?
string = "Coding For All"
substring = "Coding"

split_string = string.split()
start_coding = split_string[0] == substring
print(start_coding)

#29 Does 'Coding For All' end with a substring coding?
string = "Coding For All"
substring = "coding" # this should be false becaues the c is lowercase. If I want the word in general, then need to use .capitalize to format

split_string = string.split()
start_coding = split_string[0] == substring
print(start_coding)

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
white_space = '   Coding For All      '
print(white_space.strip())

#31 Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python
## Remember that isidentifier check if a given string is a valid identifier. An identifier in Python is a name used to identify variables, functions, classes, modules, or other objects. To be considered a valid identifier, the string must meet the following criteria:
### Start with a Letter or Underscore
### Followed by Letters, Digits, or Underscores
### Not a Reserved Keyword
### Cannot Contain Spaces or Special Characters
id_1 = "30DaysOfPython"
id_2 = "thirty_days_of_python"
print(id_1.isidentifier())
print(id_2.isidentifier())

#32  The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

joined_libs = '# '.join(libraries)
print(joined_libs)

#33 Use the new line escape sequence to separate the following sentences: I am enjoying this challenge. I just wonder what is next.

text = "I am enjoying this challenge. \nI just wonder what is next."
print(text)

#34 Use a tab escape sequence to write the following lines: Name, Age, Country, City,Asabeneh, 250, Finland, Helsinki
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsink')

#35 Use the string formatting method to display the following: radius = 10; area = 3.14 * radius ** 2; The area of a circle with radius 10 is 314 meters square.
## New styling
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius, area))

#36 Make the following using string formatting methods
'''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))