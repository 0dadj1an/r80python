#!/bin/python

import requests
import json
import pprint

#remove https warning
requests.packages.urllib3.disable_warnings()

#url = "https://192.168.248.150/web_api/"
#user = "api_user"
#pw = "demo123"




def login(url,user,pw):

	payload_list={}
	payload_list['user']=user
	payload_list['password']=pw
	headers = {
	    'content-type': "application/json",
	    'Accept': "*/*",
	}
	response = requests.post(url+"login", json=payload_list, headers=headers, verify=False)
	return response	



def add_host(sid,url,name,ip_address,groups="",comments="",nat_settings=""):
        payload_list={}
        payload_list['name']=name
        payload_list['ipv4-address']= ip_address
	if nat_settings != "":
        	payload_list['nat-settings']= nat_settings
	if groups != "" :
        	payload_list['groups']= groups 
	if comments != "":
		payload_list['comments']= comments 
	
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        print payload_list
        response = requests.post(url+"add-host", json=payload_list, headers=headers, verify=False)
        
        return response.json()

def delete_host(sid,url,name):
        payload_list={}
        payload_list['name']=name
	payload_list['ignore-warnings']="true"
        
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"delete-host", json=payload_list, headers=headers, verify=False)
        return response

def add_network(sid,url,name,subnet,mask_length,nat_settings,groups):
        payload_list={}
        payload_list['name']=name
        payload_list['subnet4']= subnet 
        payload_list['mask-length']= mask_length 
        payload_list['nat-settings']= nat_settings
        payload_list['groups']= groups            
        
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"add-network", json=payload_list, headers=headers, verify=False)
        return response.json()

def delete_network(sid,url,name):
        payload_list={}
        payload_list['name']=name

        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"delete-network", json=payload_list, headers=headers, verify=False)
        return response


def show_network_groups(sid,url):
	payload_list={}
	payload_list['details-level']="standard"
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
	    'x-chkp-sid': sid,
        }	
        response = requests.post(url+"show-groups", json=payload_list, headers=headers, verify=False)
	groups=json.loads(response.text)
	return groups

def add_network_group(sid,url,name):
        payload_list={}
        payload_list['name']=name
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"add-group", json=payload_list, headers=headers, verify=False)
        return response 

def add_members_to_network_group(sid,url,members):
        payload_list={}
        payload_list['name']=name
        payload_list['members']=members
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"set-group", json=payload_list, headers=headers, verify=False)
        return response

def add_access_layer(sid,url,name):
        payload_list={}
	payload_list['name']=name
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
	response = requests.post(url+"add-access-layer", json=payload_list, headers=headers, verify=False)	
	return response



def add_policy_package(sid,url,name,access_layer,threat_layer,comments):
        payload_list={}
        payload_list['name']=name
        payload_list['access']=access_layer
        payload_list['threat-prevention']=threat_layer
	payload_list['comments']=comments
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"add-package", json=payload_list, headers=headers, verify=False)
        return response

def add_access_section(sid,url,layer,position,name):
        payload_list={}
        payload_list['layer']=layer
        payload_list['position']=position
        payload_list['name']=name
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"add-access-section", json=payload_list, headers=headers, verify=False)
        return response

def delete_access_section_by_name(sid,url,layer,name):
        payload_list={}
        payload_list['name']=name
        payload_list['layer']=layer
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"delete-access-section", json=payload_list, headers=headers, verify=False)
        return response

def show_access_section(sid,url,layer,name):
        payload_list={}
        payload_list['layer']=layer
        payload_list['name']=name
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"show-access-section", json=payload_list, headers=headers, verify=False)
        return response
	
def add_access_rule(sid,url,layer,position,rule):
        payload_list={}
        payload_list['layer']=layer
        payload_list['position']=position
        payload_list['name']=rule['name']
	payload_list['source']=rule['source']
	payload_list['destination']=rule['destination']
	payload_list['service']=rule['service']
	payload_list['track']=rule['track']
	payload_list['action']=rule['action']
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"add-access-rule", json=payload_list, headers=headers, verify=False)
        return response

def delete_access_rule_by_rule_number(sid,url,layer,number):
        payload_list={}
        payload_list['layer']=layer
        payload_list['rule-number']=number
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"delete-access-rule", json=payload_list, headers=headers, verify=False)
        return response

def delete_access_rule_by_rule_name(sid,url,layer,name):
        payload_list={}
        payload_list['layer']=layer
        payload_list['name']=name
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"delete-access-rule", json=payload_list, headers=headers, verify=False)
        return response
	

def publish(sid,url):
        payload_list={}
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"publish", json=payload_list, headers=headers, verify=False)
        return response
       
def add_range():
	    payload_list={}
	    headers = {
			'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
			}
	    response = requests.post(url+"publish", json=payload_list, headers=headers, verify=False)
	    return response
       

def show_task(sid,url,task):
        payload_list={}
	payload_list['task-id']=task
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"show-task", json=payload_list, headers=headers, verify=False)
        return response

def logout(sid,url):
        payload_list={}
        headers = {
            'content-type': "application/json",
            'Accept': "*/*",
            'x-chkp-sid': sid,
        }
        response = requests.post(url+"logout", json=payload_list, headers=headers, verify=False)
        return response

#main program
#login and get the session id
#sid=login(url,user,pw)

#get all groups

#add policy package 
#name="my_cpx_policy2"
#comments="created by automation script"
#access_layer="true"
#threat_layer="true"
#package_return=add_policy_package(sid,url,name,access_layer,threat_layer,comments)
#print package_return

#add access rule section
#layer="my_cpx_policy2 network"
#position="top"
#position={"above":"Cleanup rule"}
#name="section1 - created by automation2"
#show_section_return=show_access_section(sid,url,layer,name)
#show_section_return=show_access_section(sid,url,layer,name)
#if show_section_return.status_code == "200":
#	print "section already exists skipping"
#else:
#	add_access_section(sid,url,layer,position,name)

#add access rule
#layer="my_cpx_policy2 network"
#position="top"
#rule={}
#rule['source']="any"
#rule['destination']="any"
#rule['service']="http"
#rule['action']="accept"
#rule['track']="Network Log"
#rule['name']="my rule 1"
#rule_response=add_access_rule(sid,url,layer,position,rule)
#print json.loads(rule_response.text)
#print rule_response

#add access rule to section
#layer="my_cpx_policy2 network"
#position={"top":"section1 - created by automation"}
#rule={}
#rule['source']="any"
#rule['destination']="any"
#rule['service']=["https","http"]
#rule['action']="accept"
#rule['track']="Network Log"
#rule['name']="my rule 2"
#rule_response=add_access_rule(sid,url,layer,position,rule)
#print rule_response
#print json.loads(rule_response.text)

#publish
#publish(sid,url)
