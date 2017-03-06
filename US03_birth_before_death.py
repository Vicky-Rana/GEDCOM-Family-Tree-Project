"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-03 Birth Before Date 
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
from all_db_operations import *
from print_data import *

def birth_before_death():
	return_flag=False
	results_for_people = get_people()
	
	for res in results_for_people:			
		if "deathDate" in res  and "birthday" in res:
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			difference_in_years = relativedelta(death_date, birthday).years
			difference= death_date.year - birthday.year
			if(difference > 0):
				return_flag=True
			else:
				return_flag=False
				message= "Birthdate is invalid for" + res["ID"]+ "Please validate the birthdate." 
				save_invalid_people_for_print(res["ID"], "US03", message)