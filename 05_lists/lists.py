# # Exercises - Day 5
# ## Exercise - Level 1
# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
anime = ['Demon Slayer','Spy X Family', 'Bleach', 'One Piece', "Mashle: Magic and Muscles", "My Hero Academia"]

# 3. Find the length of your list
print(len(anime))

# 4. Get the first item, the middle item and the last item of the list
## Get the first item
first_item = anime[0]

## Get the middle item(s)
middle_index = len(anime) // 2
middle_item = anime[middle_index]

## Get the last item
last_item = anime[-1]

print(f"First item: {first_item}")
print(f"Middle item: {middle_item}")
print(f"Last item: {last_item}")

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
## Declare a list called mixed_data_types
mixed_data_types = []

## put your(name, age, height, marital status, address)
mixed_data_types.append({'name':'Lorena'})
mixed_data_types.insert(1, {'age':'35'})
mixed_data_types.append({'height': 1.65})
mixed_data_types.append({'marital status':'None of your business'})
mixed_data_types.append({'address':'USA'})

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
## Declare a list variable named it_companies
it_companies = []

## assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
company_list = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.extend(company_list)

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
## First Company
first_company = it_companies[0]

## Second Company
second_company = len(it_companies) // 2

## Last Company
last_company = it_companies[-1]

# 10. Print the list after modifying one of the companies
it_companies.sort()
print(it_companies)

# 11. Add an IT company to it_companies
nvdia = it_companies.append('NVIDA')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'amd') 

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
## Find the index of 'amd'
index = it_companies.index('amd')

## Uppercase with .upper()
it_companies[index] = it_companies[index].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
## '#; ' as the separator
joined_itCompanies = '#; '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list.
check_amd = 'AMD' in it_companies

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
print(it_companies[::-1])
print(it_companies.reverse())

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print(len(it_companies) // 2)
print(it_companies[4])

# 21. Remove the first IT company from the list
print(it_companies.pop(0))

# 22. Remove the middle IT company or companies from the list
middle_company = len(it_companies) // 2
print(it_companies.pop(middle_company))

# 23. Remove the last IT company from the list
print(it_companies.pop())

# 24. Remove all IT companies from the list
print(it_companies.clear())

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()

index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')

## Exercise - Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age
ages.sort()
print(ages[0])
print(ages[-1])

# - Add the min age and the max age again to the list
ages.append(19)
ages.append(24)

# - Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(len(ages))

## since the list is even, the middle indices are 4 & 5
middle_index_01 = ages[4]
middle_index_02 = ages[5]

median = (middle_index_01 + middle_index_02) / 2
print(median)

# - Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(average_age)

# - Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(age_range)

# - Compare the value of (min - average) and (max - average), use abs() method
## Calculate the average age
average_age = sum(ages) / len(ages)

## Calculate the minimum and maximum age
min_age = min(ages)
max_age = max(ages)

## Compute the differences
min_diff = min_age - average_age
max_diff = max_age - average_age

## Use abs() to get the absolute values
abs_min_diff = abs(min_diff)
abs_max_diff = abs(max_diff)

# 2. Find the middle country(ies) in the countries list
## Find the middle index
middle_index = len(countries) // 2

## Get the middle country
middle_country = countries[middle_index]

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
## Find the middle index
midpoint = (len(countries) + 1) // 2

## Slice the list into two parts
first_half = countries[:midpoint]
second_half = countries[midpoint:]

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]