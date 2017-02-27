import sys
import pymongo
from collections import Counter
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




def unique_indids():
	
	individual_list = []
    
	individual = db.people.find({})
	results = [res for res in individual] 
	individual.close()
	
	
	return_flag = True
	
	for res in results:
		if res["ID"] in individual_list:
			print "Individual ID",res["ID"]," already exists","\n"
            
			return_flag = False
		else:
			individual_list.append(res["ID"])
			print "Individual ID",res["ID"]," is unique","\n"
	print (return_flag),"\n"
	return return_flag


def unique_famids():	
	family_list = []
	fam = db.family.find({})
	resul = [rest for rest in fam] 
	fam.close()
	
	return_flag = True
	for rest in resul:
		if rest["FAMID"] in family_list:
			print "Family ID already exists"
            
			return_flag = False
		else:
			family_list.append(rest["FAMID"])
			print "Family ID",rest["FAMID"]," is unique","\n"
	print (return_flag)
	return return_flag
	
	
    
if __name__ == '__main__':
    Ind_id = unique_indids()
	
if __name__ == '__main__':
    Ind_id = unique_famids()
	