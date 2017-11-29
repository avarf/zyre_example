import pyre
from pyre import Pyre


from pyre import zhelper
import zmq
import uuid
import logging
import sys
import json

n = Pyre("hp_chat")
n.join("CHAT")
n.start()

print('uuid: ', n.uuid())
print('name: ', n.name())

wsp_msg = 'MESSAGE RECEIVED'
while True:
        rec_msg = n.recv()
        print('received message: \n',str(rec_msg))
        print('end of message')
        print('message information: ')
        print('command: ', rec_msg[0].decode('utf-8'))
        # print('uuid: ', uuid.UUID(bytes=rec_msg[1]))        
        sender_uuid = uuid.UUID(bytes=rec_msg[1])
        sender_name = rec_msg[2].decode('utf-8')
        print('uuid: ', sender_uuid)
        print('sender name: ', sender_name)
        # print('sender name: ', rec_msg[2].decode('utf-8'))
        print('------ DATA ---------')
        data = rec_msg[-1]
        data = data.decode('utf-8')
        print(data)
        print('data type: ',type(data))
        print('data spec:')
        print('data length: ', len(data))
        print('------ End of Data -------')
        if str(data) == 'stop':
                print('break from the data')
                n.stop()
                break
        print('+++++++ JDATA +++++++++')
        jdata = json.dumps(data)
        jdata2 = json.loads(jdata)

#       jdata = rec_msg[-1]
        print('jdata type: ', type(jdata))
        print('jdata type 2 : ', type(jdata2))

        print('jdata: ', jdata)
        print('jdata2: ', jdata2)

        try:
                jdata4 = json.loads(data)
                print('jdata type 4 : ', type(jdata4))
                print('jdata4: ', jdata4)
        except Exception as e:
                print('Exception: ', e)
        
        # jdata4 = json.loads(data)
        # print('jdata type 4 : ', type(jdata4))
        # print('jdata4: ', jdata4)

        if len(data) > 40:
                print('INSIDE IF *******************')
                jdata3 = json.loads(data)
                print('jdata type 3 : ', type(jdata3))
                print('jdata3: ', jdata3)
                print('jdata3[car]: ',jdata3['car'])
                print('jdata3[car][car2]: ',jdata3['car']['car2'])

                # print(json.loads(jdata)['car'])
#               print(jdata2['car'])
                n.whispers(sender_uuid, wsp_msg)
                print('MESSAGE sent')
        print('+++++++ JDATA END +++++++++')
print('Finished')


