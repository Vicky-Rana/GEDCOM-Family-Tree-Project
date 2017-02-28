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
	flag = False
	#Search for individual
	individual = db.people.find({})
	for doc in individual:
		date = doc["birthday"]
		name = doc["NAME"]
		for  doc2 in individual:
			#print(doc2["NAME"])
			#print(doc2["birthday"])
			if(date == doc2["NAME"] and name == doc2["birthday"]):
				return_flag = False
			else:
				return_flag = True	
		print (return_flag)
		return return_flag

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
	return return_flag
    
if __name__ == '__main__':
    family_present = unique_name_bdate()
	
if __name__ == '__main__':
	family_date = valid_date()
	
   

