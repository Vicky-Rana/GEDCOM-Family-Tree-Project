"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: Unique Username and Birthdate 
"""
import sys
import pymongo

from pymongo import MongoClient
from pprint import pprint
#import datetime
from datetime import datetime, timedelta
from datetime import datetime
#from dateutil.relativedelta import relativedelta
#Default File Path
# MongoDB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
# Check family present for particular individual
def unique_name_bdate():
	
	#Search for individual
	individual = db.people.find({})
	results = [res for res in individual] 
	individual.close()
	print ("Printing the ID of all whose Birthday and Name is Unique and For those whose ID is repeated more than once, then the Birthday and Name of those Individuals is not Unique")
	for res in results:
		
		id = res["ID"]
		for doc2 in results:
			date = doc2["birthday"]
			name = doc2["NAME"]
			
			if(date==res["birthday"] and name==res["NAME"]):			
				number=[]
				number.append(id)

				for value in number:
					
					print(value),"\n"
					
def valid_date():
	return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()

	for res in results:			
		if "birthday" in res:
			#print("___________"+res["birthday"])
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			if (type(birthday)==datetime):
				return_flag=True
			else:
				return_flag=False
	print ("Checking if the date given is Valid or not, If true than all the bdate is valid and if false the one of the bdate is not valid")
	print (return_flag)
	return return_flag
    
if __name__ == '__main__':
    family_present = unique_name_bdate()
	
if __name__ == '__main__':
	family_date = valid_date()