import pymongo
from pymongo import MongoClient
import json
import collections
from bson import json_util
from pprint import pprint
import uuid
import logging
import sys
import time
from calendar import datetime


t = time.localtime()
current_time = str(t[0])+"-"+str(t[1])+"-"+str(t[2])+"T"+str(t[3])+":"+str(t[4])+":"+str(t[5])+"Z"


rec1 = {
    'timestamp': datetime.datetime.strptime('2017-12-10 3:25:40', "%Y-%m-%d %H:%M:%S"),
	'robotID':'r1',
	'pose':'5,8',
	'busy':'y',
	'battery':'51',
	'sensors':[{
	'IR':'1',
	'sonar':'0',
	'laser':'1',
	'microphone':'0'
	}
	],
	'motor values':[
	{
		'motor1':'8',
		'motor2':'9',
		'motor3':'9',
		'motor4':'8'
	}
	]
}

rec2 = {
    'timestamp': datetime.datetime.strptime('2017-12-10 4:25:40', "%Y-%m-%d %H:%M:%S"),
	'robotID':'r2',
	'pose':'0,0',
	'busy':'n',
	'battery':'85',
	'sensors':[{
	'IR':'1',
	'sonar':'1',
	'laser':'1',
	'microphone':'0'
	}
	],
	'motor values':[
	{
		'motor1':'7',
		'motor2':'5',
		'motor3':'5',
		'motor4':'8'
	}
	]
}

rec3 = {
    'timestamp': datetime.datetime.strptime('2017-12-10 5:25:40', "%Y-%m-%d %H:%M:%S"),
	'robotID':'r3',
	'pose':'5,15',
	'busy':'y',
	'battery':'45',
	'sensors':[{
	'IR':'1',
	'sonar':'1',
	'laser':'1',
	'microphone':'0'
	}
	],
	'motor values':[
	{
		'motor1':'9',
		'motor2':'8',
		'motor3':'9',
		'motor4':'7'
	}
	]
}

rec4 = {
    'timestamp': datetime.datetime.strptime('2017-12-10 5:26:40', "%Y-%m-%d %H:%M:%S"),
	'robotID':'r4',
	'pose':'10,6',
	'busy':'y',
	'battery':'88',
	'sensors':[
	{
		'IR':'1',
		'sonar':'0',
		'laser':'1',
		'microphone':'0'
		}
	],
	'motor values':[
	{
		'motor1':'5',
		'motor2':'9',
		'motor3':'9',
		'motor4':'6'
	}
	]
}

rec5 = {
    'timestamp': datetime.datetime.strptime('2017-12-11 5:25:40', "%Y-%m-%d %H:%M:%S"),
	'robotID':'r5',
	'pose':'10,9',
	'busy':'n',
	'battery':'88',
	'sensors':[
	{
	'IR':'1',
	'sonar':'0',
	'laser':'1',
	'microphone':'0'}
	],
	'motor values':[
	{
	'motor1':'9',
	'motor2':'6',
	'motor3':'8',
	'motor4':'7'
	}
	]
}


# another way to work with mongodb
# database["test"].insert({'name': 'foo'})
#     doc = database["test"].find_one({'name': 'foo'})
#     return json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)

con = MongoClient()
# creating database
db = con.test_db

# result = db.members.delete_many({'busy':'n'})



# members is a collection
# result = db.members.insert_one(rec1)
# result = db.members.insert_one(rec2)
# result = db.members.insert_one(rec3)
# result = db.members.insert_one(rec4)
# result = db.members.insert_one(rec5)

# docs = db.members.find()
# for d in docs:
# 	print(d)

print('////////////////////////////////////////////////////')
# getting a query between two timestamp
# 2017-12-10T3:25:40Z
# 2017-12-11T5:25:40Z
start_time = datetime.datetime.strptime("2017-12-10 3:55:40", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime("2017-12-10 11:25:40", "%Y-%m-%d %H:%M:%S")
print(start_time)
print(end_time)


# start_time = "2017-12-10 3:55:40"
# end_time = "2017-12-10 11:25:40"
# print(datetime.datetime.strptime("2017-12-10 3:25:40", "%Y-%m-%d %H:%M:%S"))
# extract subset of key-values of returned query
docs = db.members.find({'timestamp': {'$gte': start_time, '$lt': end_time}}, {'robotID':1, 'sensors':1, 'timestamp':1})
for doc in docs:
	print(doc)
print('////////////////////////////////////////////////////')
# create the response from the whole query result
query_results = db.members.find({'timestamp': {'$gte': start_time, '$lt': end_time}}, {'robotID':1, 'sensors':1, 'timestamp':1})
# query_results = []
# for doc in docs:
# 	print(doc)
# 	query_results.append(doc)
# query_results = [*docs]
query_results = [*query_results]

# print(type(docs))

print(type(query_results))
print(len(query_results))
# print(query_results)
print(query_results[1])
print(query_results[0])


print('////////////////////////////////////////////////////')
# Getting a query and change it to jason and prepare it for sending it over zyre
# q1 = db.members.find({'busy':'y'})
# answer = []
# for q in q1:
# 	print(type(q))
# 	q = json.dumps(q, sort_keys=True, indent=4, default=json_util.default)
# 	jq = q.encode('utf-8')
# 	answer.append(jq)
# print(len(answer))
# print(answer[1])
print('////////////////////////////////////////////////////')

# Getting the feilds of the first record of the database and convert it to a list 
feilds = [*db.members.find({})[0].keys()]
print(feilds)
print(type(feilds))
print('////////////////////////////////////////////////////')

# TO DO:
# is a LIST is good for our purpose or we need this in json format???

# TO DO:
# Get query between two timestamps


print('Finished')


# TO DO:
# THE SOLUTION: we have to create a list of one dict and work with it as follow:
# jd['motor values'][0]['motro2']
# definition:
# 'motor values':[{
# 	'motro2':'9',
# 	'motro2':'5'
# }]
# I have to define the records as dict of dict instead of list of dict because of having access to them
# in dict of dict we can write: jd['motor values']['motro2']
# but in list of dict we have to write: jd['motor values'][1]
