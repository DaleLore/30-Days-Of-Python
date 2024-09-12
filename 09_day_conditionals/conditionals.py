# Exercises - Day 9
## Exercise Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 

## Get user input
age = int(input("Enter your age: "))

## IF ELSE statement
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more year(s) to be old enough to drive.")
    

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

## User input
your_age = int(input("Enter your age: "))

## Define my age
my_age = int(input("I'm ")) 

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1: 
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age!")


# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
number_1 = int(input("Enter number one: "))
number_2 = int(input("Enter number two: "))

if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
elif number_1 < number_2:
    print(f"{number_1} is less than {number_2}")
else:
    print(f"{number_1} is equal to {number_2}")


## Exercise Level 2
# 1. Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

# Get the student's score
score = float(input("Enter the student's score: "))

if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("C")
elif 50 <= score < 60:
    print("D")
elif 0 <= score < 50:
    print("F")
else:
    print("invalid score")


# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season = str(input("What month is it? "))

if (season == "September" or  "October" or "November"):
    print("Autumn")
elif (season == "December" or  "January" or "February"):
    print("Winter")
elif (season == "March" or  "April" or "May"):
    print("Spring")
elif (season == "June" or  "July" or "August"):
    print("Summer")
else:
    print("Choose a month: ")

# 3. The following list contains some fruits: 
## If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Which fruit do you like? ").lower()

if (user_fruit in fruits):
    print("Yum!")
else:
    fruits.append(user_fruit)
    print(f"{user_fruit.lower()} has been added to the list.")
    print("Updated list of fruits:", fruits)

## Exercise Level 3
# 4. Modify this person dictionary
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
 }

## * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    # Check if 'Python' is one of the skills
    if 'Python' in person['skills']:
        print("The person has 'Python' as a skill.")
    else:
        print("The person does not have 'Python' as a skill.")
else:
    print("'Skills' key not found in the person dictionary.")

## * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person:
    # Check if 'Python' is in the list of skills
    if 'Python' in person['skills']:
        print('The person has Python skill.')
    else:
        print('The person does not have Python skill.')
else:
    print('Skills key is not present in the dictionary.')

## * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'skills' in person:
    skills = person['skills']
    
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills and len(skills) == 3:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills and len(skills) == 3:
        print('He is a fullstack developer')
    else:
        print('Unknown title')
else:
    print('Skills key is not present in the dictionary.')

## * If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.

if person.get('married') and person.get('country') == 'Finland':
    print(f"{person['name']} lives in Finland. He is married.")
else:
    print("Conditions not met for the specified output.")


