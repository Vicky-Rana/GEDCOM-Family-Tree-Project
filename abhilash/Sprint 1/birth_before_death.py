"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: Birth Before Date 
"""
from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
#from collections import counter
import re
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def birth_before_death():
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()
	print("\t SPRINT 1: USER SOTRY : BIRTHDATE SHOULD BE BEFORE DEATH")
	for res in results:			
		if "deathDate" in res  and "birthday" in res:
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			difference_in_years = relativedelta(death_date, birthday).years
			
			difference= death_date.year - birthday.year
			if(difference > 0):
				return_flag=True
			else:
				return_flag=False
	if (return_flag==True):
		print("All Individuals have Birthdate Before Deathdate...!")
	else:
		print("Few Individuals have Birthdate Before Deathdate... Please modify the records in GEDCOM")	
	print (return_flag)
	return return_flag

def valid_date():
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()

	for res in results:			
		if "deathDate" in res  and "birthday" in res:
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			if (type(death_date)==datetime and type(birthday)==datetime):

				return_flag=True
			else:
				return_flag=False

	print (return_flag)
	return return_flag


if __name__ == '__main__':
    a= birth_before_death()
    