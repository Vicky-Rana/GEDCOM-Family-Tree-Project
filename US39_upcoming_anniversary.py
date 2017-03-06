"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-39 List Upcoming Anniversary 

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

def upcoming_anniversary():
	
	return_flag=False
	results_for_family = get_family()
	current=datetime.now()
	fw=open('upcoming_anniversaries.txt','w')
	fw.write('\n--------------------------------')
	fw.write('\n LIST OF UPCOMING ANNIVERSARIES')
	fw.write('\n--------------------------------')
	for res in results_for_family: 
			
		if "marriage" in res:
			anniversary= datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
			if (anniversary.month- current.month   > 0 ):
				return_flag=True
				fw.write("\n"+res["FAMID"]+"\t"+res["marriage"]+"\n")
				
			elif (anniversary.month- current.month==0 & anniversary.day - current.day >0):
				return_flag=True
				print(res["FAMID"] + res["NAME"]+res["marriage"])
				fw.write(res["FAMID"]+"\t"+res["marriage"])
			else:
				return_flag=False
				message="Anniversary has passed for"+res["FAMID"]
				save_invalid_family_for_print(res["FAMID"], "US39", message)

	return return_flag

if __name__ == '__main__':
    
    b= upcoming_anniversary()
    