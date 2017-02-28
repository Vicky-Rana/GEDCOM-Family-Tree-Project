import sys
import pymongo

from pymongo import MongoClient
from pprint import pprint
import datetime
from datetime import datetime, timedelta
from datetime import datetime
#from dateutil.relativedelta import relativedelta
#Default File Path
# MongoDB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

print("\n-----------------------------------------------------------")
print ("SPRINT 1: USER STORY: UNIQUE NAME AND BIRTHDAY")
print("\n-----------------------------------------------------------")

# Check family present for particular individual
def unique_name_bdate():
	
	#Search for individual
	individual = db.people.find({})
	results = [res for res in individual] 
	individual.close()
	print("Checking in Individual Collection for Uniqueness ")
	print("\n."*3)
	for res in results:
		
		id = res["ID"]
		for doc2 in results:
			date = doc2["birthday"]
			name = doc2["NAME"]
			idd = doc2["ID"]
					
			if(date==res["birthday"] and name==res["NAME"] and idd!=id ):
				number=[]
				number.append(id)
				for value in number:
					print ("Printing the ID of the Individual whose Birthday and Name is Not Unique")
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
	print (return_flag)
	print("All the Individuals have unique name and Birthdate....")
	print("If that would have been false ..program prints the ID and NAME of such individuals separately..")

	return return_flag
    
if __name__ == '__main__':
    family_present = unique_name_bdate()
	
if __name__ == '__main__':
	family_date = valid_date()
	
 