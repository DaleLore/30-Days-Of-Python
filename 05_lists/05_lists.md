<!-- Day 5: 30 Days of python programming -->

# Exercises - Day 5
## Exercise - Level 1
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using print()
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;  '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:
    - front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    - back_end = ['Node','Express', 'MongoDB']
27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

## Exercise - Level 2
1. The following is a list of 10 students ages:
```ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]```
    - Sort the list and find the min and max age
    - Add the min age and the max age again to the list
    - Find the median age (one middle item or two middle items divided by two)
    - Find the average age (sum of all items divided by their number )
    - Find the range of the ages (max minus min)
    - Compare the value of (min - average) and (max - average), use abs() method

2. Find the middle country(ies) in the countries list
3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

# Notes - Lists
- There are four collection data types in Python:
    - List
    - Tuple
    - Set
    - Dictionary

## Lists
- A list is a collection that is ordered and can be modified
- A list will also allow duplicate members
- A list can be empty or it may have different data type items in it

### How to Create a List
- Using list built-in function: list()
- Using square brackets: list = []
- List with initial values: 
    - anime = ['Demon Slayer','Spy X Family', 'Bleach', 'One Piece' ]
    - print('Anime:', anime)
    - type(anime)
    - len(anime)
- Lists can have items of different data types: 
    - list_example = ['string', 10, True, {'date_type':'Dictionary'}]

### Accessing List Items Using Positive Indexing
- We can access each item in a list using their index
- REMEMBER: A list index starts from 0

### Accessing List Items Using Negative Indexing
- Negative indexing means beginning from the end so -1 refers to the last item, -2 refers to the second to last item

### Unpacking List Items
```
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst

print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

### Slicing Items from a List
- With positive indexing, we can specify a range of positive indexes by specifying the start, end, and step. Then the return value will be a new list
```
fruits = ['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[0:4]    # start = 0; will do all the fruits since there are only 4
all_fruits = fruits[0:]     # start = 0; will do all in list
```

- With negative indexing, we can specify a range of negative indexes by specifying the state, end and step. Then the return value will be a new list
```
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]
```

### Modifying Lists
- Lists are mutable so they can be modified
```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado' # will change the 0 index to avocado; bye banana
print(fruits)
```

### Checking Items in a List
- Checking an item if it is a member of a list using the <i>in</i> operator
- Using <i>in</i> will result in True or False
```
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
doesnt_exit = 'lime' in fruits
print(doesnt_exit)
```

### Adding / Removing Items to a List
- Adding items to the end of an existing list with append()
    - Syntax: lst.append(item)
    - fruits.append('pineapple')
- Inserting items to a specified index in a list with insert()
    - Syntax: lst.insert(index, item)
    - Example: fruits.insert(2, 'apple')
- Removing specified items from a list with remove()
    - Syntax: lst.remove(item)
    - Example: fruits.remove('banana')
- Removing specified indexed items from a list with pop()
    - Syntax: lst.pop(index)
    - Example: fruits.pop(0)
- Removing specified indexed items from a list with the keyword <i>del</i>; can also delete items within index range; can also delete the list completely
    - Syntax: del lst[index] OR del lst
    - Example: del fruits[0]
    - Example: del fruits

### Clearing List Items
- Emptying the list with clear()
    - Formula: lst.clear()
    - Example: fruits.clear()

### Copying Lists
- Copy a list by reassigning it to a new variable: list2 = list1
    - NOTE: Any changes we make in list2 will also modify the original list, list1
- Copying a list that won't modify the original list: copy()

### Joining Lists
- Join (or concatenate) two or more lists with plus operator (+)
    - Syntax: list3 = list1 + list2
    - Example:  fruits = ['banana', 'orange', 'mango', 'lemon']
                vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
                fruits_and_vegetables = fruits + vegetables
- Joining lists using extend(); this allows you to append lists in a list
    - Syntax: list1.extend(list2)
    - Example:  num1 = [0, 1, 2, 3]
                num2= [4, 5, 6]
                num1.extend(num2)
                print('Numbers:', num1)

### Counting Items in a List
- Count items with count() to return the number of times an item appears in a list
    - Syntax: lst.count(item)
    - Example:  ages = [22, 19, 24, 25, 26, 24, 25, 24]
                print(ages.count(24))

### Finding Index of an Item
- Find items with index() to return the index of an item in the list
    - Syntax: lst.index(item)
    - Example:  fruits = ['banana', 'orange', 'mango', 'lemon']
                print(fruits.index('orange'))

### Reversing a List
- Reverse a list with reverse() to reverse the order of a list
    - Syntax: lst.reverse()
    - Example:  fruits = ['banana', 'orange', 'mango', 'lemon']
                fruits.reverse()

### Sorting List Items
- Sort lists with sort() to reorder the list items in ascending order
    - NOTE: THIS WILL MODIFY THE ORIGINAL LIST
    - Syntax:   lst.sort() # ascending
                lst.sort(reverse=True) # descending
    - Example:  fruits = ['banana', 'orange', 'mango', 'lemon']
                fruits.sort()
- Sort lists with sorted() to return the ordered list; this will NOT modify the original list
    - Syntax:   lst.sorted()
    - Example:  fruits = ['banana', 'orange', 'mango', 'lemon']
                print(sorted(fruits))