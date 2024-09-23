<!-- Day 22: 30 Days of python programming -->

# Exercises - Day 22

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

