from pymongo import MongoClient
import datetime


myClient = MongoClient()
db = myClient.pythondb
users_db = db.users
user1 = {
            "username": "Luke",
            "password": "my_password",
            "favourite_colour": "Blue",
            "languages": [
                "scala",
                "java",
                "python",
                "c",
                "c#"
            ]
        }
user_id = users_db.insert_one(user1).inserted_id

users = [{"username": "third", "password": "12345"}, {"username": "fourth", "password": "54321"}]
users_db.insert_many(users)

print(str(users_db.find({"favourite_colour": "Blue"}).count()))
print(str(users_db.find({"favourite_colour": "Blue", "username": "Muth"}).count()))

current_date_time = datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 11)
users_db.insert_one({"username": "Bob", "date": current_date_time})
print(str(users_db.find({"date": {"$gt":  old_date}}).count()))
"""
gt = greater than
gte = greater than or equal to
lt = less than
lte = less than or equal to
exists = returns a boolean, according to if it exists or not
ne = not equal to
"""
