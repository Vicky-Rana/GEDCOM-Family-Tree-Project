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
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']








def check_marriagebeforedivorce():
	
	
	#Search Family
	fam1 = db.family.find({})
	
	results = [res for res in fam1] 
	fam1.close()
	
	for res in results:
		if "marriage" and "divorce" in res:
			#print "Marriage_Date------",res["marriage"]
			#print "Divorce_Date------",res["divorce"]
			marr = res["marriage"]
			divv = res["divorce"]
		
			#newdate1 = time.strptime(marr, "%d/%m/%Y")
			#newdate2 = time.strptime(divv, "%d/%m/%Y")
			if marr > divv:
			
				message = "Divorced date "+str(divv)+", Before Marriage date "+str(marr)+ " , therefore it is not valid."
				save_invalid_family_for_print(res["FAMID"], "US04", message)



	

	

			
