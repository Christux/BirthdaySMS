#!/usr/bin/env python
# -*- coding: utf8 -*-
# author	: Christux
# copyright	: Copyright 2015
# license	: GPL

import datetime
from Data import database
from SMS import sms

class notificationSMS():

	def __init__ (self,database,sms):
		self.database=database
		self.sms=sms
	
	# Sends the notification SMS
	def run(self):
		if self.database.notification() != "":
			resp=self.sms.send(self.database.notification())
			print(str(datetime.date.today())+": "+self.database.notification().replace("\n"," ")+" Server: "+self.sms.respAnalysis(resp.status))
		return

# Main function		
if __name__ == '__main__':
	# Reads the database in 'List.dat', see format
	base=database("List.dat")
	# Init the http request
	sms=sms("username","password")
	# Sends the SMS
	notificationSMS(base,sms).run()
	# Close http connection
	sms.close()