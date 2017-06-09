#!/bin/python

import csv
import r80_apis
import json
import ConfigParser

#########################
#get login credentials
#########################

config = ConfigParser.ConfigParser()
config.read('cp.ini') #read from cp.ini file
url=config.get('config','url',0)
#print url
user=config.get('config','user',0)
pw=config.get('config','password',0)


#################
# read csv file
#################

with open('hosts.csv') as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:
		#print row['name'] , row['ip'], row['type'], row['comments'] , row['group']
		print "add host name "'"'+row['name']+'"'" ip-address "'"'+row['ip']+'"'" groups.1 "'"'+row['group']+'"'" comments "'"'+row['comments']+'"'
		




