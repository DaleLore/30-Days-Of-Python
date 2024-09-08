# ## Exercise - Level 1
# 1. Create an empty tuple
empty_tpl = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
anime_sisters = ('Nezuko', 'Teiko')     # anime_sisters = ('Nezuko') <- this WONT work. cause this isn't a tuple; its a string; it WILL yell at you
anime_brothers = ('Genya', 'Senjuro', 'Yuichiro')

# 3. Join brothers and sisters tuples and assign it to siblings
anime_siblings = anime_sisters + anime_brothers
print(anime_siblings)

# 4. How many siblings do you have?
print(len(anime_siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
## REMEMBER: Tuples are IMMUTABLE; you can only change it into a list in order to add more names
anime_sibling_list = list(anime_siblings)
anime_mother = anime_sibling_list[1] = 'Kie'
anime_sibling_list[1] = anime_mother
print(anime_sibling_list)

tuple_again = tuple(anime_sibling_list)
print(type(tuple_again))

# ## Exercise - Level 2
# 1. Unpack siblings and parents from family_members
family_members = ('Nezuko', 'Kie', 'Genya', 'Senjuro', 'Yuichiro')
sibling, parent, *more_siblings = family_members
print("Parent: ", parent)
print("Siblings: ", sibling, more_siblings)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('spinach', 'mushrooms', 'peppers')
animal_products = ('beef', 'pork', 'chicken')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
# middle_item = fruits_and_veggies[middle_index]
middle_item = food_stuff_lt[middle_index: middle_index + 1]

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
#     - Check if 'Estonia' is a nordic country
#     - Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estonia_present = 'Estonia' in nordic_countries
print(estonia_present)
iceland_present = 'Iceland' in nordic_countries
print(iceland_present)