<!-- Day 8: 30 Days of python programming -->

# Exercises - Day 8
1. Create an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using items() method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries


# Notes
- A dictionary is a collection of unordered, modifiable paired (key:value) data types.

## What can be done with dictionaries
- To create a dictionary,
    - We use curly brackets, {}, to create a dictionary
    - We can also use Python's built-in function, `dict()`
        - Syntax: empty_dict = {}
        - Example: dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

- Like with other data types, you can check the length of a dictionary byt checking the number of 'key: value' pairs in it
``` 
print(len(dct))
```

- You can access Dictionary items by referring to its key name
    - Note: If the item does not exist, Python will raise an error (aka it will yell at you)
    - To avoid this error, we can first check if the key exists with `get()`; if the item isn't there, the get method will return None
```
print(dct['key1'])      # value1
print(dct['key4'])      # value4
print(dct['key5'])      # Error
print(dct.get('key5'))  # None
```

- Adding items to the dictionary means adding a key AND a value to create one item
```
dct['key5'] = 'value5'
print(dct)
```

- Modifying items in a dictionary is the same syntax as adding items, choose the key:value pair you want to change, and change the value
```
dct['key5'] = 'value five'
print(dct)
```

- You can still use the `in()` operator to check if a key exists in the dictionary
```
print('key2' in dct)    # True
print('key5' in dct)    # False
```

- There are different ways to remove a key:value pair from a dictionary
    - pop(key): removes the item with the specified key name
    - popitem(): remove the last item
    - del[]: removes an item with specified key name

```
dct.pop('key1')     # removes key1 item
dct.popitem()       # removes the last item
del dct['key2']     # removes key2 item
```

- Changing a dictionary to a list of tuples is done with `items()`
```
print(dct.items())
```

- Clearing items can be done with `clear()`
```
print(dct.clear())
```

- Delete the entire dictionary with `del`
```
del dct
```

- The `copy()` method allows you to copy the dictionary avoiding any mutation of the original
```
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
```

- Getting dictionary keys as a list has a specific method called, `keys()`, which gives us all the keys of a dictionary as a list
```
keys = dct.keys()
print(keys) 
```

- Getting the specific values as a list is done with `values()`, and similar with `keys()`, the values will be returned as a list
```
values = dct.values()
print(values)
```
