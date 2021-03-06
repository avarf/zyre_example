'''
Zyre communication (sender) in python using Pyre library
This program connects to a zyre group and when we decided 
it starts to get a serries of queries from another program 
that we choose.   

Author: Mohammadali Varfan
Contact information: varfanm@live.com
'''

import pyre
from pyre import Pyre

from pyre import zhelper
import zmq
import uuid
import logging
import sys
import json

n = Pyre("sender_node")
print('Join group [CHAT]')
n.join("CHAT")

print('node START')
n.start()

print('node uuid: ', n.uuid())
print('node name: ', n.name())

nodes_list = dict()
msg_data = {
  "header": {
    "type": "CMD",
    "version": "0.1.0",
    "metamodel": "ropod-msg-schema.json",
    "msg_id": "0d05d0bc-f1d2-4355-bd88-edf44e2475c8",
    "timestamp": "2017-11-11T11:11:00Z"
  },
  "payload": {
    "metamodel": "ropod-demo-cmd-schema.json",
    "commandList":[
      { 
        "command": "GOTO",
        "location": "START"
      }
     ]
  }
}

queries = [{ 
        "command": "GOTO",
        "location": "MOBIDIK"
      },
      { 
        "command": "GOTO",
        "location": "START"
      },
      { 
        "command": "GOTO",
        "location": "ELEVATOR"
      },
      { 
        "command": "POSE"
      },
      { 
        "command": "RESUME",
      },
      { 
        "command": "STOP",
      }]

msg_name_request = 'NameRequest'
dest_name = "receiver_node"
get_queries = True
send_next_query = True
k = 0
q = 0

print('press enter to start the program')
k = input()

# send an order to all nodes(shout) to send their names
n.shout("CHAT", msg_name_request.encode('utf-8'))

while get_queries:
	rec_msg = n.recv()
	msg_type = rec_msg[0].decode('utf-8')

	# get all the nodes in the group
	sender_uuid = uuid.UUID(bytes=rec_msg[1])
	sender_name = rec_msg[2].decode('utf-8')
	nodes_list[sender_name] = sender_uuid

	data = rec_msg[-1]
	data = data.decode('utf-8')
	if str(msg_type) == 'SHOUT' or str(msg_type) == 'WHISPER':
		try:
			jdata = json.loads(data)
			if jdata['payload']['answerList'][0]['command'] == "ANSWER":
				send_next_query = True
				print('received answer:')
				print(jdata['payload']['answerList'])
		except Exception as e:
			# print('Exception: ', e)
			pass

	# If we get an answer for the previous query we send the next one
	if send_next_query:
		# print("start sending query")
		msg_data['payload']['commandList'][0] = queries[q]
		jmsg_data = json.dumps(msg_data).encode('utf-8')
		dest_uuid = nodes_list[dest_name]
		n.whisper(dest_uuid, jmsg_data)
		send_next_query = False
		q += 1
		if q == len(queries):
			get_queries = False


n.stop()
print('Program Finished')