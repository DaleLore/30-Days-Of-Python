<!-- Day 22: 30 Days of python programming -->

# Exercises - Day 22
- [beautifulsoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.


# Notes - Web Scraping
- What is web scrapping? Web scraping in Python is the process of automatically extracting data from websites using Python libraries and tools

- Web scraping involves:
    - Sending an HTTP Request to the site
    - Parsing the HTML
    - Extracting the data
    - Storing the data in a format like CSV, JSON or a database

- Python packages needed:
    - `requests`
    - `beautifulSoup4`
    - `website`

```
# Install packages in terminal first
pip install requests
pip install beautifulsoup4
```

```
# Import packges in .py file
import requests
from bs4 import BeautifulSoup
```

```
# syntax for web scraping
## import packages
import requests 
from bs4 import BeautifulSoup

## declare website
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url
response = requests.get(url)

# check the status of site
status = response.status_code # i.e. 200, 404, 500
print(status) # 200 means the fetching was successful

# store site request in a response
response = requests.get(url)

# store response content into a variable to parse 
content = response.content

# BeautifulSoup will start the parsing
soup = BeautifulSoup(content, 'html.parser')

# Figure out what you got
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

# put into table
tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)
```
