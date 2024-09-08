# Exercises: Day 7 
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## Exercise - Level 1
# 1. Find the length of the set it_companies
len(it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
more_companies = {'NVDIA', 'AMD'}
it_companies.update(more_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

# 5. What is the difference between remove and discard
## Remove will yell at you if the item isn't found in the set
it_companies.remove('Twitter')

## Discard will not do anything if the item isn't found in the set
it_companies.discard('Twitter')

## Exercise - Level 2
# 1. Join A and B
C = A.union(B)

# 2. Find A intersection B
A.intersection(B)

# 3. Is A subset of B
A.issubset(B)

# 4. Are A and B disjoint sets
A.isdisjoint(B)

# 5. Join A with B and B with A
## note: Its the same
print(A.union(B))
print(B.union(A))

# 6. What is the symmetric difference between A and B
A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B

## Exercise - Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
len(age)
age_set = set(age)
len(age_set)

# 2. Explain the difference between the following data types: string, list, tuple and set
## A string is an immutable, indexed, ordered sequence of characters enclosed within single, double, or triple quotes.
string = "Hello, Python!"

## A list is an ordered, mutable collection of any data type (integers, strings, other lists, etc.)
list = [1, "apple", 3.14, [5, 6, 7]]

## A tuple is an ordered BUT immutable collection of elements
tuple = (1, "banana", 3.14)

## A set is an unordered, mutable collection of unique elements
set = {1, 2, 3, 4}

# 3. `I am a teacher and I love to inspire and teach people.` How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'

split_sentence = sentence.split()
unique_words = set(split_sentence)
unique_word_count = len(unique_words)

print("Unique words:", unique_words)
print("Number of unique words:", unique_word_count)