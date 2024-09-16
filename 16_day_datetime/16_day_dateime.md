<!-- Day 16: 30 Days of python programming -->

# Exercises - Day 16

# Notes - DateTime
- Python has got `datetime` module to handle date and time

```
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

- With dir or help built-in commands it is possible to know the avaible funcitons in a certain module
- The datetime module has many fuctions, but the main one's we'll focus on are: `date`, `datetime`, `time`, and `timedelta`

## Getting datetime information 
- Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC
```
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
```

## Formatting Date Output Using `strftime`
- The `strftime()` function is used to format `datetime` objects into readable string representations
- It allows you to convert a `datetime` object into a formatted string according to a specified format using various format codes
- Documentation can be found here in the [Python strftime cheatsheet](https://strftime.org/)
```
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
```

## String to Time Using `strptime`
- The strptime() function prses a string representing a date and/pr time into a datetime object
- The function takes two arguments: the date/time string and the format in which the string is structured
- Programiz has a page specifically on Python's [strptime](https://www.programiz.com/python-programming/datetime/strptime)
```
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# Example
date_string = 5 December, 2019
date_object = 2019-12-05 00:00:00
```

## Using `date` from `datetime`
- The `date` class needs to be imported `datetime` module
- The `date()` constructor takes three arguments: year, month, and day
```
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

## Time Objects to Represent Time
- The `time()` class from the `datetime` module is used to represent time (hour, minute, seconds, and microseconds) independent of the date
- To use the `time` class, you need to import it from the `datetime` module
- The `time()` constructor gets passed an hour, minute, second, and an optional microsecond, as arguments
```
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```

## Difference Between Two Points in Time Using `timedelta`
- In Python, you can calculate the difference between two points in time using date objects from the datetime module. 
- This difference is represented as a `timedelta` object, which gives you the number of days between the two dates.
    - Create two `date` objects
    - Subtract one `date` from the other, which gives a `timedelta` object
    - Access the `days` attribute of the `timedelta` object to get the number of days

```
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```