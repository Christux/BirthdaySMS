#!/usr/bin/env python
# -*- coding: utf8 -*-
# author	: Christux
# copyright	: Copyright 2015
# license	: GPL

import httplib

# Class for sending SMS using Free API
class sms():

	def __init__(self,username,password):
		self.server = "smsapi.free-mobile.fr"
		self.username = username
		self.password = password
		self.connection = httplib.HTTPSConnection(self.server) # Opens connection to SMS server

	# Closes connection
	def close(self):
		self.connection.close()

	# Sends message
	def send(self,message):
		order="/sendmsg?user="+self.username+"&pass="+self.password+"&msg="+message.replace(" ","%20").replace("\n","%0d")
		self.connection.request("GET", order)
		resp = self.connection.getresponse()
		return resp
	
	# Returns server result	
	def respAnalysis(self,status):
		result="unexpected result"
		if status == 200:
			result="success"
		if status == 400:
			result="parameter missing"
		if status == 402:
			result="too many SMS..."
		if status == 403:
			result="service unavailable for user, or wrong credentials"
		if status == 500:
			result="server error"
		return result


# Main function for testing
if __name__ == '__main__':
	notification=sms("username","password")
	resp = notification.send("Hello World !\nHo Boy")
	notification.close()
	print(resp.status, resp.reason)
	print(notification.respAnalysis(resp.status))
