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


def living_marriages():
	family=db.family.find({})
	results = [res for res in family] #count = cursor.count()
	family.close()

	for res in results: 
		wife_age = 0
		husband_age = 0
		if "marriage" in res:
			marriage_date = datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
			if "HUSBAND" in res and "WIFE" in res: 
				living_marriage = True
				husband = db.people.find({"ID" : res["HUSBAND"]})
				result_for_husband = [doc for doc in husband]
				wife =  db.people.find({"ID" : res["WIFE"]})
				result_for_wife = [doc1 for doc1 in wife]
				for doc in result_for_husband:
					if "deathDate" in doc:
						living_marriage = False;
					else:
						living_marriage = True;
				for doc1 in result_for_wife:
					if "deathDate" in doc1:
						living_marriage = False;
					else:
						living_marriage = True;
				if living_marriage:
					print("This is living marriage")
				else:
					print("This is non-living marriage")
		
if __name__ == '__main__':
    check_birth_before_marriage = living_marriages()