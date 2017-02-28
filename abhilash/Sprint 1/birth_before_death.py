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
	print("\n-----------------------------------------------------------")
	print("\t SPRINT 1: USER SOTRY : BIRTHDATE SHOULD BE BEFORE DEATH")
	print("\n-----------------------------------------------------------")
	print("Checking if any of the died person has birth before death....")
	print("\n."*3)
	print("List of Dead Inidividuals")
	print("\n-----------------------------------------------------------")
	print("\n")
	for res in results:			
		if "deathDate" in res  and "birthday" in res:
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			difference_in_years = relativedelta(death_date, birthday).years
			print(res["NAME"])
			print(res["birthday"]+ res["deathDate"])
			difference= death_date.year - birthday.year
			if(difference > 0):
				return_flag=True
			else:
				return_flag=False
	print("Checking if any of the living person has birth before death....")
	print("\n."*3)
	print("\n-----------------------------------------------------------")
	print("\nList of Living Individuals")
	print("\n-----------------------------------------------------------")
	for res in results:
		if "birthday" in res and "deathDate" not in res:
			print (res["NAME"]) 
			print(res ["birthday"])
	print("\n-----------------------------------------------------------")
	if (return_flag==True):
		print("This GEDCOM has contains all the Birthdates before Deathdates ")	
	else:
		print("Few Individuals have Birthdate Before Deathdate... Please modify the records in GEDCOM")	
	print("\n-----------------------------------------------------------")
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
    