# This follows along this tutorial: 
# http://api.mongodb.com/python/current/tutorial.html

# MongoDB installation procedure:
# https://docs.mongodb.com/v4.0/tutorial/install-mongodb-on-windows/

from pymongo import MongoClient
client = MongoClient()

db = client.test_database
print(db)

# make a dict
import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

# insert this document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
# print(post_id)
# this ID key is automatically added if the doc does not contain already an _id key. 

# after this insertion, the posts-collection has been created on the server. 
print(db.collection_names(include_system_collections=False))

# Queries:
# the simplest is find_one()
import pprint
pprint.pprint(posts.find_one())

# query specific element:
pprint.pprint(posts.find_one({"author": "Joris"}))

# skipped thing about querieing by _id tag, useful in web applications

# bulk import:
new_posts = [{"author": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14)},
            {"author": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)

print(result.inserted_ids)

# querying for more than one document: find() returns a cursor, over which we can iterate
for post in posts.find():
    pprint.pprint(post)

# counting
print(posts.count_documents({}))

# i can also follow this one: https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
