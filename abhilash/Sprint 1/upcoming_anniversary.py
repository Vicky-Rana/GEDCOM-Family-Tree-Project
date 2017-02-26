"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: List Upcoming Anniversary
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

def upcoming_anniversary():
	
	return_flag=False
	family=db.family.find({})
	results = [res for res in family] #count = cursor.count()
	family.close()

	current=datetime.now()
	for res in results: 
			
		if "marriage" in res:
			anniversary= datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
			if (anniversary.month- current.month   > 0 ):
				return_flag=True
				print(res["FAMID"])
				print(res["marriage"])

			elif (anniversary.month- current.month==0 & anniversary.day - current.day >0):
				return_flag=True
				print(res["FAMID"])
				print(res["marriage"])
			else:
				return_flag=False
	return return_flag

if __name__ == '__main__':
    a= upcoming_birthday()
    b= upcoming_anniversary()
    