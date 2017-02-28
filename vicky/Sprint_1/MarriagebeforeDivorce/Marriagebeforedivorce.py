

import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#DB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']








def check_marriagebeforedivorce():
	
	return_flag = False
	#Search Family
	fam1 = db.family.find({})
	
	results = [res for res in fam1] 
	fam1.close()
	
	for res in results:
		if "divorce" in res:
			print "Marriage_Date------",res["marriage"]
			print "Divorce_Date------",res["divorce"]
			marr = res["marriage"]
			divv = res["divorce"]
		
			#newdate1 = time.strptime(marr, "%d/%m/%Y")
			#newdate2 = time.strptime(divv, "%d/%m/%Y")
			if marr > divv:
			
				print "Marriage Date and Divorce Date for Husband ID",res["HUSBAND"],"and Wife ID",res["WIFE"],"is not correct","\n"
			else:
				print "Marriage Date and Divorce Date for Husband ID",res["HUSBAND"],"and Wife ID",res["WIFE"],"is correct","\n"



	
	
if __name__ == '__main__':
    marrbeforediv = check_marriagebeforedivorce()
	

			
