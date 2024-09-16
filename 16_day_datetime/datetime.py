# # Exercises - Day 16
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print(now)
# 2. Format the current date using this format: ("%m/%d/%Y, %H:%M:%S")

# 3. Today is 5 December, 2019. Change this time string to time.

# 4. Calculate the time difference between now and new year.

# 5. Calculate the time difference between 1 January 1970 and now.

# 6. Think, what can you use the datetime module for? Examples:
#     - Time series analysis
#     - To get a timestamp of any activities in an application
#     - Adding posts on a blog


### Note
### Naming the file datetime.py confused Python. `This is being imported instead of the standard library module, because the directory of the main script is the first place Python looks for imports.`
### Resource https://stackoverflow.com/questions/15975517/cant-import-import-datetime-in-script