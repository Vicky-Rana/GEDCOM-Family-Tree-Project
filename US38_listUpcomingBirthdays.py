from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
from print_data import *
from all_db_operations import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']


def upcoming_birthday():
	
	#return_flag=False
	people=db.people.find({})
	results = [res for res in people] 
	people.close()

	current=datetime.now()
	print(current.month)
	for res in results: 
			
		if "birthday" in res:
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			if (birthday.month- current.month   > 0 ):
				#return_flag=True
				print(res["ID"])
				print(res["NAME"])
				print(res["birthday"])

			elif (birthday.month- current.month== 0 & birthday.day > current.day):
				#return_flag=True
				print(res["ID"])
				print(res["NAME"])
				print(res["birthday"])
				#return_flag=False
	#return return_flag
upcoming_birthday()