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


def age_less_150():
	
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()

	for res in results: # while index != count //This will iterate the list without you needed to keep a counter:
    # doc = cursor[index] // No need for this since 'res' holds the current record in the loop cycle
	#Check age for dead person 
			
		if "deathDate" in res  and "birthday" in res:
			#print ("Bday"+res["deathDate"])
			#print( "Date"+res["birthday"])
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			#rint(type(birthday))
			difference_in_years = relativedelta(death_date, birthday).years
			#c=a.year-b.year
			#print(c)
			#print(difference_in_years)
			#print("ID"+res["ID"]+":") 

			if death_date.year -birthday.year <150: 
				return_flag= True
				#print(return_flag)
			else:
				return_flag= False
				#print(return_flag)
	print(return_flag)
	return return_flag

def if_birthdate_present():
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()

	for res in results:			
		if "birthday" in res:
			return_flag= True
			#print(return_flag)
		else:
			return_flag= False
			#print(return_flag)
	print(return_flag)
	return return_flag

def if_deathdate_present():
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()

	for res in results:			
		if "deathDate" in res:
			return_flag= True
			#print(return_flag)
		else:
			return_flag= False
			#print(return_flag)
	print(return_flag)
	return return_flag

def age_diffe_non_negative():
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()

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
    a= age_less_150()
    b= if_birthdate_present()
    c= if_deathdate_present()
    d= age_diffe_non_zero()
    e=valid_date()