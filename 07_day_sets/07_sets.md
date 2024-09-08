<!-- Day 7: 30 Days of python programming -->

# Exercises - Day 7
## Exercise - Level 1
## Exercise - Level 2
## Exercise - Level 3


# Notes - Sets
- A set is a collection of unordered and unindexed distinct elements
- In Python, a set is used to store unique items
- Sets support various operations that allow you to combine, compare, and analyze the relationships between sets:
    - Union (| or union()): Combines all unique elements from two or more sets
        ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        union_set = set1 | set2
        ```

    - Intersection (& or intersection()): Returns the common elements that exist in both sets
        ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        intersection_set = set1 & set2
        ```

    - Difference (- or difference()): Returns the elements in the first set that are not in the second set
        ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        difference_set = set1 - set2
        ```

    - Symmetric Difference (^ or symmetric_difference()): Returns the elements that are in either of the sets, but not in both (i.e., the union of sets minus their intersection)
         ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        sym_diff_set = set1 ^ set2
        ```

    - Subset (<= or issubset()): A set is a subset if all elements of the first set exist in the second set
        ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        is_subset = set1 <= set2
        ```
                    
    - Superset (>= or issuperset()): A set is a superset if it contains all elements of another set
        ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        is_superset = set1 >= set2
        ```
                    
    - Disjoint Set (isdisjoint()): Two sets are disjoint if they have no elements in common
        ```
        set1 = {1, 2, 3}     
        set2 = {3, 4, 5}
        is_disjoint = set1.isdisjoint(set2)
        ```

## What you can do with a set
- You can create a set using the `set()` built-in function
```
set_example = set()
set_example = {'item1', 'item2', 'item3', 'item4'}
```

- You can get the length of the set using `len()`
```
len(set_example)
```

- You can access items in a set using `in`
```
print("Does set set_example contain item3? ", 'item3' in set_example)
```

- You can add items to a set with `add()`
```
set_example.add('item5')
```

- You can update the items with `update()`
```
set_example.update(['item5','item6','item7'])
```

- You can add multiple items to a set with `update()`
```
set_example.update(['item5','item6','item7'])
```

- Remove an item from a set using `remove()`. NOTE that if the item is not found using remove(), it will raise errors (and yell at you)
```
set_example.remove('item2')
```

- You can also remove an item using `discard()` and it won't yell at you if the item isn't found
```
set_example.discard('item5')
```

- Remove a random item from a list using `pop()`
```
set_example.pop()
```

- Clear or empty a set with `clear()`
```
set_example.clear()
```

- Completely delete a set with the `del` operator
```
del set_example
```

- Converting a list to a set is possible! Converting list to set removes duplicates and only unique items will be reserved
- These sets will have the items in a random order because sets in general are unordered
```
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'}
```

- It's possible to join two sets using the `union()` or `update()` methods
    - The union method returns a new set
    - The update methods inserts a set into a given set; it will modify the original
```
set_01 = {'item1', 'item2', 'item3', 'item4'}
set_02 = {'item5', 'item6', 'item7', 'item8'}
set_03 = set_01.union(set_02)
set_01.update(set_02)           
```

- Finding intersection items means that the `intersection()` method will return a set of items which are in both the sets
```
set_01 = {'item1', 'item2', 'item3', 'item4'}
set_02 = {'item3', 'item2'}
set_01.intersection(set_02) # {'item3', 'item2'}
```

- Checking subset and super sets
    - `issubset()`: A set is considered a subset of another set if all elements of the first set are contained in the second set
    - `issuperset()`: A set is considered a superset of another set if it contains all elements of the second set

```
set1 = {1, 2}
set2 = {1, 2, 3, 4}

is_subset = set1.issubset(set2)      # Yes because items 1 and 2 are in set2
is_superset = set1.issuperset(set2)  # No
```

- Checking the difference between two sets with `difference()`
```
set_1 = {'item1', 'item2', 'item3', 'item4'}
set_2 = {'item2', 'item3'}
set_2.difference(set_1) 
set_1.difference(set_2)
```

- Finding symmetric difference between two sets can be done with `symmetric_difference()`
    - It returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

```
set_1 = {'item1', 'item2', 'item3', 'item4'}
set_2 = {'item2', 'item3'}

set_2.symmetric_difference(set_1)
```

- Joining Sets can be done if two sets do not have a common item or items we call them disjoint sets. 
    - We can check if two sets are joint or disjoint using `isdisjoint()` method

