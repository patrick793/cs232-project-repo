import json
import sys

out_file = open(sys.argv[1], "w")
data = []
with open('tweets_1.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_2.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_3.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_4_1.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_4_2.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_4_3.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_4_4.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_5.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_6.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())
with open('tweets_7.csv.json', 'r', encoding='utf8') as data_file:
	data = data + json.loads(data_file.read())


out_file.write(json.dumps(data))