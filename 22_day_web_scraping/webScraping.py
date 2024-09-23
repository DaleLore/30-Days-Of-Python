# # Exercises - Day 22

import requests
from bs4 import BeautifulSoup

# 1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# ## checking the status
# response = requests.get(url)
# status = response.status_code
# print(status)

# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
## Note - archive.ics.uci.edu/datasets.php is not found so just using the previous URL

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

# 3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

