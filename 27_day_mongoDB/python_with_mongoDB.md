<!-- Day 27: 30 Days of python programming -->

# Exercises - Day 27 


# Notes - Python with MongoDB
- Python is a backend technology and it can be connected with different data base applications
- It can be connect to both SQL and noSQL databases

## MongoDB
- MongoDB is a NoSQL database
- MongoDB stores data in a JSON like document, which makes MongoDB very flexlible and scalable
- To use MongoDB, you need to sign up: [monogodb.com](https://www.mongodb.com/)
- The following table shows the dfferences between SQL versus NoSQL database

| SQL    | NoSQL |
| -------- | ------- |
| Database  | Database    |
| Tables | Collections     |
| Rows    | Documents    |
| Columns    | Fields    |
| Index    | Index    |
| Join    | Embedding and Linking    |
| Group By    | Aggregation    |
| Primary Key    | _id field    |

## Getting Connection String (MongoDB URI)
- Copy the connection string link and you will get something like this: 
```
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

- Python needs a mongoDB driver to access the mongoDB database
- We'll use _pymongo_ with _dnspython_ to connect our application with mongoDB base
- Inside your project directory, install pymongo and dnspython
    - The "dnspython" module most be installed to use mongodb+srv://URIs
    - The dnspython is a DNS toolkit for Python
    - It supports almost all records types
```
pip install pymongo dnspython
```

## Connecting Flask application to MongoDB Cluster
- 
- Once you run the code, you will receive a default mongoDB database
```
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

## Creating a database and collection
- A database and collection in mongoDB will be created if it doesn't exist
- Name the database _thirty days of python_ and _student_ collection
- To create a database
```
db = client.name_of_databse # we can create a database like this or the second way
db = client['name_of_database']

# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```
