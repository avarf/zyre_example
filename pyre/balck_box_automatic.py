"""
I also need a seprate file for filing the database
sender: sends a jason message with command query and the feild that we need to get query like:
query - robotID   
receiver: receiver decodes th command and when it is query just reads the query type from the received messaged and get the query and returned the answer in a jason format
sender: after receiving the query answer we print the query and send a new message for new query   
receiver:  
sender:   
receiver:  
sender:   
receiver:  
sender:   
receiver:  
sender:   
receiver:  
"""


from pymongo import MongoClient


# receiver code
con = MongoClient()
db = con.test_db

