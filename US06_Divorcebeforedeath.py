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
#DB connection
#connection = MongoClient('localhost', 27017)
#db = connection['GEDCOMDB']



def divorcebeforedeath():
	
	
	#Search Family
	
	
	
	results = get_family() 
	
	for res in results:
		if ("HUSBAND" or "WIFE") and "divorce" in res:
			#print("___________"+res["HUSBAND"])
			#print("___________"+res["WIFE"])
			husband = res["HUSBAND"]
			wife = res["WIFE"]
			
			indi = get_people()
			for temp in indi:
				if husband == temp["ID"] and "deathDate" in temp:
					deathdth = temp["deathDate"]
					divdateh = res["divorce"]
					if divdateh > deathdth:
						
					

			
						message = "Divorced date "+str(divdateh)+", After Husband id "+str(husband)+ " Death on "+str(deathdth)+", therefore Divorce is not valid."
						save_invalid_family_for_print(res["FAMID"], "US06", message)
	
				if wife == temp["ID"] and "deathDate" in temp:
					deathdt = temp["deathDate"]
					divdate = res["divorce"]
					if divdate > deathdt:
						
						
						message = "Divorced date "+str(divdate)+", After Wife id "+str(wife)+ " Death on "+str(deathdt)+", therefore Divorce is not valid."
						save_invalid_family_for_print(res["FAMID"], "US06", message)
		


			
