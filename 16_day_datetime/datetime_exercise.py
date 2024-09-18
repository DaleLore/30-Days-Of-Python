# # Exercises - Day 16
from datetime import datetime

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)

# 2. Format the current date using this format: ("%m/%d/%Y, %H:%M:%S")
todays_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(todays_date)

# 3. Today is 5 December, 2019. Change this time string to time.
# Date string
date_string = "5 December, 2019"

# Convert the date string to a datetime object
date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)

# 4. Calculate the time difference between now and new year.
# Define the New Year date and time
new_year = datetime(now.year + 1, 1, 1) # This is (1 [January], 1 [first], 1 [now.year + 1])

# Calculate the time difference
time_difference = new_year - now

print("Time difference until New Year:", time_difference)

# I don't want the microseconds cause it looks ugly
formatted_difference = str(time_difference).split('.')[0]
print("Time difference until New Year:", formatted_difference)

# 5. Calculate the time difference between 1 January 1970 and now.
# Define the starting date (January 1, 1970)
start_date = datetime(1970, 1, 1)

# Calculate the time difference
time_difference_1970 = now - start_date

# Format the time difference without microseconds
formatted_difference_1970 = str(time_difference_1970).split('.')[0]

print("Time difference from January 1, 1970 to now:", time_difference_1970)

# 6. Think, what can you use the datetime module for? 
# Examples:
#     - Time series analysis
#           - with time series analysis I can analyze and manipulate time-based data, such as financial data, sensor data, or any data indexed by time.
#     - To get a timestamp of any activities in an application
#     - Adding posts on a blog
#     - Scheduling and automation by creating and managing schedules, reminders, and automated tasks to run at specific times
#     - Time zone handling!


### Note
### Naming the file datetime.py confused Python. `This is being imported instead of the standard library module, because the directory of the main script is the first place Python looks for imports.`
### Resource https://stackoverflow.com/questions/15975517/cant-import-import-datetime-in-script