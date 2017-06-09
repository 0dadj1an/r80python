#!/bin/python

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
#add host
################
name="mg123"
ip_address="1.1.1.10"
comments="done by automation"

host=r80_apis.add_host(sid,url,name,ip_address,"",comments,"")
print json.loads(host.text)

################
#publish
################
print "publish output:"
print "=============="
publish=r80_apis.publish(sid,url)
print json.loads(publish.text)

time.sleep(5)
################
#logout
################
logout=r80_apis.logout(sid,url)

print "=============="
print "logout output"
print "=============="
print json.loads(logout.text)

