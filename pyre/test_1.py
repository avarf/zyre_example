import pyre
from pyre import Pyre


from pyre import zhelper 
import zmq 
import uuid
import logging
import sys
import json


print('Pyre START')
n = Pyre("acer_node")

# n.set_header("CHAT_Header1","example header 1")
# n.set_header("CHAT_Header2","example header 2")

print('join')
n.join("CHAT")

print('node START')
n.start()

print('uuid: ', n.uuid())
print('name: ', n.name())

#n.set_name('Acer_Node')
#print('name: ', n.name())

# send by name
# n.whisper('9371B3', 'Hello from the Acer_Node')

# print(n.peers())

msg = 'Hello from acer'
dic_msg =  { "name":"John", "age":30, "car":"bmw" }
jmsg = json.dumps(dic_msg).encode('utf-8')
lst_msg = ['physics', 'Biology', 'chemistry', 'maths']
lst_msg = [x.encode('utf-8') for x in lst_msg]
stp_msg = 'stop'
k = 0
while True:
    print('insert command: ')
    k = input()
    print(k)
    if str(k) == 'q':
    	print('break')
    	n.stop()
    	break
    elif str(k) == 'm':
        print('send message')
        # n.shout("CHAT", msg.encode('ascii'))
        n.shout("CHAT", msg.encode('utf-8'))
        # n.shout("CHAT", msg.decode('ascii'))
    elif str(k) == 's':
        print('stop message sent')
        n.shout("CHAT", stp_msg.encode('utf-8'))
    elif str(k) == 'l':
        print('LIST message sent')
        # n.shout("CHAT", lst_msg.encode('utf-8'))
        n.shout("CHAT", lst_msg)
        # n.shout("CHAT", [x.encode('utf-8') for x in lst_msg])
    elif str(k) == 'dic':
        n.shout("CHAT", dic_msg.encode('utf-8'))
    elif str(k) == 'js':
        n.shout("CHAT", jmsg)
    else:
    	print('nodes list')
    	print(n.peers())



print('Finished')
"""
def chat(ctx, pipe):
	n = Pyre("CHAT")

	n.set_header("CHAT_Header1","example header 1")
	n.set_header("CHAT_Header2","example header 2")
	
	n.join("CHAT")
	n.start()

"""





"""

#  Constructor, creates a new Zyre node. Note that until you start the
#  node it is silent and invisible to other nodes on the network.
node = pyre.Pyre()

#  Set node header; these are provided to other nodes during discovery
#  and come in each ENTER message.
node.set_header(name, value)

#  (TODO: Currently a Pyre node starts immediately) Start node, 
# after setting header values. When you start a node it
#  begins discovery and connection.
node.start()

#  Join a named group; after joining a group you can send messages to
#  the group and all Zyre nodes in that group will receive them.
node.join(group)

#  Leave a group
node.leave(group)

#  Receive next message from network; the message may be a control
#  message (ENTER, EXIT, JOIN, LEAVE) or data (WHISPER, SHOUT).
#  Returns a list of message frames
msgs = node.recv();

# Send message to single peer, specified as a UUID object (import uuid)
# Destroys message after sending
node.whisper(peer, msg)

# Send message to a named group
# Destroys message after sending
node.shout(group, msg);

#  Send string to single peer specified as a UUID string.
#  String is formatted using printf specifiers.
node.whispers(peer, msg_string)

#  Send message to a named group
#  Destroys message after sending
node.shouts(group, msg_string);
"""
