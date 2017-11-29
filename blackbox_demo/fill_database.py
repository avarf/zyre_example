'''
Fill the database with some dummy data for using in the demo

Author: Mohammadali Varfan
Contact information: varfanm@live.com
'''

from pymongo import MongoClient
import json

class Mongodb_wrapper(object):
	"""A class for working with mongodb"""

	def __init__(self):
		self.con = MongoClient()

	def make_database(self, db_name):
		self.db = self.con.db_name

	def insert_data(self, data):
		self.db.insert_one(data)

	def insert_data(self, data, collection_name):
		self.db.collection_name.insert_one(data)

	def query_data(self, query_feilds, collection_name):
		records = self.db.collection_name.find()
		for r in records:
			print(r)

	def delete_record(self, record):
		pass




query_feilds = {
"firstname" : "jane",
"surname" : "doe"
# "score" : { "$gt" : 0 }
}

d1 = {
	'name': 'Ali',
		'family':'varfan',
		'sex':'male',
		'mem_id': '1'
}

d2 = {
	'name': 'Selale',
		'family':'Ozbay',
		'sex':'female',
		'id':'2'
}

query_format = {
	"command":"answer/getquery",
	"data": "information",
	"data2": {"car1":"Ford","car2":"bmw", "car3":"Fiat"}
}

query_format2 = {
	"command":"answer/getquery",
	"data": "information",
	"data2": {"car1":"Ford","car2":"bmw", "car3":"Fiat"}
}

jquery = json.dumps(query_format2)
# jquery = json.loads(str(query_format))

# mw = Mongodb_wrapper()
# mw.make_database('ds_test')
# mw.insert_data(d2,'members')
# mw.insert_data(d1,'members')
# mw.query_data('a','members')

print(d2)
d2['id'] = '55'
print(d2)
print(d2['name'])

print(query_format["data"])
print(query_format["data2"]["car2"])

# before I can call json feilds normally I have to load it using json.loads
jquery = json.loads(jquery)
print(jquery['command'])
print(jquery['data2']['car2'])
print(jquery["data2"]["car3"])
print('------------------------------')

if 'car2' in jquery['data2']:
	print(jquery['data2']['car2'])
	print('------------------------------')
data = {
  "header": {
    "type": "CMD",
    "version": "0.1.0",
    "metamodel": "ropod-msg-schema.json",
    "msg_id": "0d05d0bc-f1d2-4355-bd88-edf44e2475c8",
    "timestamp": "2017-11-11T11:11:00Z"
  },
  "payload": {
    "metamodel": "ropod-demo-cmd-schema.json",
    "commandList": [
      { 
        "command": "GOTO",
        "location": "START"
      }
      ,{ 
        "command": "GOTO",
        "location": "MOBIDIK"
      }
    ]
  }
}

dddd = {
	"command": "POSE",
	"location": "Homeeeee"
}

data['payload']['commandList'][0] = dddd

jdata = json.dumps(data)
jdata = json.loads(jdata)

# jdata['payload']['commandList'][0]['location'] = "Homeeeee"


for item in jdata['payload']['commandList']:
	if 'command' in item and item['command'] == "POSE":
		print('+++++++++++++')
		print(item['command'])
		print(item['location'])


q = [{ 
        "command": "GOTO",
        "location": "MOBIDIK"
      },
      { 
        "command": "GOTO",
        "location": "MOBIDIK"
      },
      { 
        "command": "GOTO",
        "location": "MOBIDIK"
      }]
q[1] = dddd

print('q1',q[1])
print('Finished')