import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
URL = 'https://example.com/jobs'
response = requests.get(URL)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the data you're interested in
job_titles = soup.find_all('h2', class_='job-title')

# Step 4: Extract and store the job titles
jobs = [job.text.strip() for job in job_titles]

# Optional: Store the data in a DataFrame (using pandas)
df = pd.DataFrame(jobs, columns=['Job Title'])

# Step 5: Export the data to a CSV file
df.to_csv('job_titles.csv', index=False)

print(f"Scraped {len(jobs)} job titles successfully.")
