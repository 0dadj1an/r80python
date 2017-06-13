#!/bin/python

import csv
import r80_apis
import json
import ConfigParser
import time

#########################
#get login credentials
#########################

config = ConfigParser.ConfigParser()
config.read('cp.ini') #read from cp.ini file
url=config.get('config','url',0)
print url
user=config.get('config','user',0)
pw=config.get('config','password',0)


#################
#login to CP API
#################
sid_return=r80_apis.login(url,user,pw)
print "status code"
print sid_return.status_code
if sid_return.status_code == 200:
        print "this"
        sid_text=json.loads(sid_return.text)
        sid = sid_text['sid']
        print "========="
        print "sid"
        print sid
        print "========="
else:
        print "else"
        print json.loads(sid_return.text)
        exit


#################
# read csv file
#################

with open('hosts.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
         natsettings ={}
         print row['name'] , row['ip'], row['type'], row['comments'] , row['group'],
         host=r80_apis.add_host(sid,url,row['name'],row['ip'],"", row['comments'],"")
         print host
        
################
#publish
################
publish=r80_apis.publish(sid,url)
print json.loads(publish.text)

publish_text=json.loads(publish.text)
show_task=r80_apis.show_task(sid,url,publish_text['task-id'])
print json.loads(show_task.text)

#####################
# wait for publish to finish
#u'tasks': [{u'task-id': u'01234567-89ab-cdef-a197-071c6ce706e3', u'task-name': u'Publish operation', u'status': u'in progress', u'progress-percentage': 0, u'suppressed': False}]}
#####################


show_task_text=json.loads(show_task.text)
while show_task_text['tasks'][0]['status'] == "in progress":
	print " publish status = ", show_task_text['tasks'][0]['progress-percentage']
	time.sleep(3)
	show_task=r80_apis.show_task(sid,url,publish_text['task-id'])
	show_task_text=json.loads(show_task.text)
print " publish status = ", show_task_text['tasks'][0]['progress-percentage'] , show_task_text['tasks'][0]['status']


################
#logout
################
logout=r80_apis.logout(sid,url)



