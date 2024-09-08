# Exercises: Day 8 - Dictionaries

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Niko", 
    "color": "Brown", 
    "breed": "Mix", 
    "legs": 4, 
    "age": 3
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Buckminster", 
    "last_name": "Fuller", 
    "gender": "Male", 
    "age": 88, 
    "matiral_status": 'married',
    "skills": 'architect',
    "country": 'USA', 
    "city": 'Milton', 
    "address": 'Somewhere in Massachusetts', 
}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
# Get the value of "skills"
skills_value = student["skills"]
print(skills_value)
type(skills_value)

# 6. Modify the skills values by adding one or two skills
student['skills'] = 'architect', 'writer', 'theorist'
student['skills'] = 'designer' # this will overwrite everything

# 7. Get the dictionary keys as a list
st_keys = student.keys()
print(st_keys)

# 8. Get the dictionary values as a list
st_values = student.values()
print(st_values)

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())

# 10. Delete one of the items in the dictionary
student.pop('skills')
print(student)

# 11. Delete one of the dictionaries
del student 

