from pymongo import MongoClient
import json

# c = MongoClient('mongo1,mongo2,mongo3', 27017, replicaset='tweets')
c = MongoClient(port=27017)
db = c.tweets

#result = db.test.insert_one({'test':'testing'})

#print(result)

data = []
democrats = 0
republicans = 0
with open('tweets.json', 'r', encoding='utf8') as data_file:
	data = json.loads(data_file.read())

for tweet in data:
	result = db.tweets.insert_one(tweet)
	if tweet['rooted_for'] == 'Republican':
		republicans += 1
	else:
		democrats += 1

	print(result)
	print("R : " + str(republicans) + ", D : "+ str(democrats))

print("Done..!")
print("Republicans : " + republicans)
print("Democrats : " + democrats)

