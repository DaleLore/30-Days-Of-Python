<!-- Day 6: 30 Days of python programming -->

# Exercises - Day 6
## Exercise - Level 1
1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

## Exercise - Level 2
1. Unpack siblings and parents from family_members
2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
3. Change the about food_stuff_tp tuple to a food_stuff_lt list
4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
5. Slice out the first three items and the last three items from food_staff_lt list
6. Delete the food_staff_tp tuple completely
7. Check if an item exists in tuple:
    - Check if 'Estonia' is a nordic country
    - Check if 'Iceland' is a nordic country
    - ```nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')```

# Notes - Tuples
- A tuple is a collection of different data types
    - A tuple is ordered
    - Unlike a list, a tuple is unchangeable; you can't add, insert, remove or change its value at all
- Tuples are written with round brackets , ()
- Tuples have fewer methods than lists

- Built-in Methods
    - tuple(): to create an empty tuple
    - count(): to count the number of a specified item in a tuple
    - index(): to find the index of a specified item in a tuple
        - operator: to join two or more typles and to create a new tuple

## Creating a Tuple
- Empty tuple
    - Syntax: empty_tuple = ()
    - Syntax (constructor): empty_tuple = tuple()
- Tuple with initial values
    - tpl = ('item1', 'item2','item3')

## Tuple Length
- You can use the same len() method on typles
    - Syntax:   tpl = ('item1', 'item2', 'item3')
                len(tpl)

## Accessing Tuple Items
- Similar with the list data type, you can use positive or negative indexing to access tuple items
- Positive indexing:
    - Syntax:   tpl = ('item1', 'item2', 'item3')
                first_item = tpl[0]
                second_item = tpl[1]
    
- Negative indexing:
    - Syntax:   tpl = ('item1', 'item2', 'item3','item4')
                first_item = tpl[-4]
                second_item = tpl[-3]

## Slicing tuples
- You can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple
- The return value will be a new tuple with a specified items
- Range of Positive Indexes:
    - Syntax:   tpl = ('item1', 'item2', 'item3','item4')
                all_items = tpl[0:4]         # all items
                all_items = tpl[0:]         # all items
                middle_two_items = tpl[1:3]  # does not include item at index 
- Range of Negative Indexes:
    - Syntax:   tpl = ('item1', 'item2', 'item3','item4')
                all_items = tpl[-4:]         # all items
                middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

## Changing Tuples to Lists
- We can change tuples to lists and lists to tuples
- REMEMBER: Tuples are immutable so if we want to modify a tuple we should change it to a list
    - Syntax:   tpl = ('item1', 'item2', 'item3','item4')
                lst = list(tpl)

## Checking an Item in a Tuple
- We can check if an item exists or not in a tuple using <i>in</i>
- This returns a boolean
    - Syntax:   tpl = ('item1', 'item2', 'item3','item4')
                'item2' in tpl # True

## Joining Tuples
- We can join two or more tuples using the plus operator (+)
     - Syntax:  tpl1 = ('item1', 'item2', 'item3')
                tpl2 = ('item4', 'item5','item6')
                tpl3 = tpl1 + tpl2

## Deleting Tuples
- It is NOT possible to remove a single item in a tuple
- BUT it is possible to delete the tuple itself using <i>del</i>


