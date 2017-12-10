import pymongo
from pymongo import MongoClient
import json
import collections
from bson import json_util
from pprint import pprint


rec1 = {
	'robotID':'r1',
	'pose':'5,8',
	'busy':'y',
	'battery':'51',
	'sensors':[
	{'IR':'1'},
	{'sonar':'0'},
	{'laser':'1'},
	{'microphone':'0'}
	],
	'motor values':[
	{
		'motro1':'8',
		'motro2':'9',
		'motro3':'9',
		'motro4':'8'
	}
	]
}

rec2 = {
	'robotID':'r2',
	'pose':'0,0',
	'busy':'n',
	'battery':'85',
	'sensors':[
	{'IR':'1'},
	{'sonar':'1'},
	{'laser':'1'},
	{'microphone':'0'}
	],
	'motor values':[
	{
		'motro1':'7',
		'motro2':'5',
		'motro3':'5',
		'motro4':'8'
	}
	]
}

rec3 = {
	'robotID':'r3',
	'pose':'5,15',
	'busy':'y',
	'battery':'45',
	'sensors':[
	{'IR':'1'},
	{'sonar':'1'},
	{'laser':'1'},
	{'microphone':'0'}
	],
	'motor values':[
	{
		'motro1':'9',
		'motro2':'8',
		'motro3':'9',
		'motro4':'7'
	}
	]
}

rec4 = {
	'robotID':'r4',
	'pose':'10,6',
	'busy':'y',
	'battery':'88',
	'sensors':[
	{'IR':'1'},
	{'sonar':'0'},
	{'laser':'1'},
	{'microphone':'0'}
	],
	'motor values':[
	{
		'motro1':'5',
		'motro2':'9',
		'motro3':'9',
		'motro4':'6'
	}
	]
}

rec5 = {
	'robotID':'',
	'pose':'',
	'busy':'',
	'battery':'',
	'sensors':[
	{'IR':'1'},
	{'sonar':'0'},
	{'laser':'1'},
	{'microphone':'0'}
	],
	'motor values':[
	{'motro1':''},
	{'motro2':''},
	{'motro3':''},
	{'motro4':''}
	]
}


# another way to work with mongodb
# database["test"].insert({'name': 'foo'})
#     doc = database["test"].find_one({'name': 'foo'})
#     return json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)

con = MongoClient()
# creating database
db = con.test_db

# members is a collection
# result = db.members.insert_one(rec1)
# result = db.members.insert_one(rec2)
# result = db.members.insert_one(rec3)
# result = db.members.insert_one(rec4)


print('---------------------------')
# result = db.members.delete_many({'busy':'y'})
docs = db.members.find()
# for d in docs:
# 	# jd = json.dumps(d)
# 	jd = json.dumps(d, sort_keys=True, indent=4, default=json_util.default)
# 	# jd = json.loads(d)
# 	print(jd)

jd = json.dumps(docs[0], sort_keys=True, indent=4, default=json_util.default)
jd = json.loads(jd)

pprint(jd)
print('--------------')
print(jd['battery'])
print('--------------')
print(jd['motor values'][0]['motro2'])
print('--------------')


# for d in docs:
# 	pprint(d)

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
