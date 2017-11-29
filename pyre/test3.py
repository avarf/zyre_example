d = { "name":"John", "age":30, "car":"bmw" }

b = 'new key'

if b not in d:
	d[b] = 'new val'
else:
	print(d[b])
	
print(d)

ddd = dict()
ddd[b] = 'adgadgadeg'
print(ddd)