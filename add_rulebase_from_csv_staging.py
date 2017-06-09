#!/bin/python

import csv
import r80_apis
import json
import ConfigParser

####################
# global params
####################

position={"above":"Implicit Cleanup Rule"}
layer="sko-automation-demo network"


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

with open('rules.csv') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
                print row['name'], row['source'], row['destination'] , row['service'] , row['action'] , row['track'], row['comment'], row['type']
		if row['type'] == "section_tittle":
			#add section tittle
			section_response=r80_apis.add_access_section(sid,url,layer,position,row['name'])
		if row['type'] == "rule":
			rule={}
			#source
			if '|' in row['source']:
				rule['source']=row['source'].split('|')

			else:
				rule['source']=row['source']
			#destination
			if '|' in row['destination']:
				rule['destination']=row['destination'].split('|')
			else:
				rule['destination']=row['destination']
			#service
			if '|' in row['service']:
				rule['service']=row['service'].split('|')
			else:
				rule['service']=row['service']
			#non multi-value fields
			rule['action']=row['action']
			rule['track']=row['track']
			rule['name']=row['name']
			#add rule
			rule_response=r80_apis.add_access_rule(sid,url,layer,position,rule)
			print rule_response
			print json.loads(rule_response.text)
		

################
#publish
################
publish=r80_apis.publish(sid,url)
print json.loads(publish.text)

################
#logout
################
logout=r80_apis.logout(sid,url)



