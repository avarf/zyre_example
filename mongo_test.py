from pymongo import MongoClient
import json


# col_name = 'database'
# con = MongoClient()
# db = con.col_name



d1 = {
	'name': 'Ali',
		'family':'Varfan',
		'sex':'male',
		'id': 1
}

d2 = {
	'name': 'Selale',
		'family':'Ozbay',
		'sex':'female',
		'id': 2
}

d3 = {
	'name': 'Bita',
		'family':'Varfan',
		'sex':'female',
		'id':3
}

# db.col_name.insert_one(d1)
# db.col_name.insert_one(d2)
# db.col_name.insert_one(d3)

# db.col_name.delete_many({'sex':'female', 'family': 'Varfan'})

q = ["name", "family"]

# res = db.col_name.find({'sex':'female'})
# for r in res:
# 	print(r)

# print('---------')

# res = db.col_name.find({'sex':'female', 'id': { '$gte': 3}}, {'name' : 1, 'family' : 1})
# for r in res:
# 	print(r)



features = []
for f in q:
	features.append({f:1})
print(features)