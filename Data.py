#!/usr/bin/env python
# -*- coding: utf8 -*-
# author	: Christux
# copyright	: Copyright 2015
# license	: GPL

import datetime

# Single person class
class person():

	def __init__(self,name,day,month,year):
		self.name=name
		self.day=int(day)
		self.month=int(month)
		self.year=int(year)
	
	# Calculates age at present time
	def age(self,date):
		if date.day>=self.day and date.month>=self.month:
			return date.year-self.year
		else:
			return date.year-self.year-1
	
	# Determines if birthday at present time	
	def isToday(self,date):
		if date.day==self.day and date.month==self.month:
			return 1
		else:
			return 0

	# Prints name and birth date
	def disp(self):
		print(self.name+'\t'+str(self.day)+'/'+str(self.month)+'/'+str(self.year))

# Set of person objects, reading file
class database():
	
	def __init__(self,datafile):
		self.today=datetime.date.today()
		self.file=datafile
		self.persons=self.readfile()
		self.bday_list=self.check()
	
	# Reads people list	
	def readfile(self):
		
		data = []
		
		f = open(self.file,'r')
		lines = f.readlines()
		f.close()
		
		# File analysis
		for i in range(0,len(lines)):
			
			# Ignore comment lines
			if not lines[i].startswith("#"):
			
				var = lines[i].strip().split(';')
				name = var[0]
				bdate = var[1].split('/')
				day = bdate[0]
				month = bdate[1]
				year = bdate[2]
			
				# Add personn to database
				data.append(person(name,day,month,year))
			
		return data
	
	# Return birthday people list at present time
	def check(self):
		bday = []
		for i in range(0,len(self.persons)):
			if self.persons[i].isToday(self.today) == 1:
				bday.append(i)
		return bday
	
	# Return number of birthday at present time
	def nBday(self):
		return len(self.bday_list)
	
	# Disp birthday list
	def disp_bday(self):
		for i in range(0,len(self.bday_list)):
			self.persons[self.bday_list[i]].disp()
		return
	
	# Disp people list	
	def disp(self):
		for i in range(0,len(self.persons)):
			self.persons[i].disp()
		return	
	
	# Return SMS message	
	def notification(self):
		message=""
		for i in range(0,len(self.bday_list)):
			person=self.persons[self.bday_list[i]]
			age = person.age(self.today)
			
			# If age is not known
			if age >= self.today.year:
				#message=message+person.name+" fête aujourd'hui son anniversaire."
				message=message+"It is " + person.name+" birthday."
			
			# Else age is printed	
			else:
				#message=message+person.name+" fête aujourd'hui ses "+str(age)+" ans."
				message=message+"It is " + person.name + " " + str(age)+"th birthday."
			
			# Skip a line between several birthdays
			if i < len(self.bday_list) -1:
				message=message+"\n\n"
		
		return message
			
			
# Main function for testing
if __name__ == '__main__':
	Me = person("Me","21","01","1974")
	Me.disp()
	print(Me.isToday(datetime.date.today()))
	print(Me.age(datetime.date.today()))
	
	base = database("List.dat")
	base.disp()
	print("Birthday:")
	base.disp_bday()
	print("SMS:")
	print(base.notification())
	
	