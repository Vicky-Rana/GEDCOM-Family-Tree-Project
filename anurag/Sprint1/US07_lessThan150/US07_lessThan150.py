from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
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

	for res in results: 
			
		if "deathDate" in res  and "birthday" in res:
			
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			
			difference_in_years = relativedelta(death_date, birthday).years
			
			if death_date.year -birthday.year <150: 
				return_flag= True
			
			else:
				return_flag= False
			
	#print(return_flag)
	return return_flag


if __name__ == '__main__':
    a= age_less_150()
    