

import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#DB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']








def check_marriagebeforedeath():
	
	
	#Search Family
	fam1 = db.family.find({})
	
	
	results = [res for res in fam1] #count = cursor.count()
	fam1.close()
	
	for res in results:
		if ("HUSBAND" or "WIFE") and "divorce" in res:
			#print("___________"+res["HUSBAND"])
			#print("___________"+res["WIFE"])
			husband = res["HUSBAND"]
			wife = res["WIFE"]
			
			indi = db.people.find({})
			for temp in indi:
				if (husband == temp["ID"] or wife == temp["ID"]) and "deathDate" in temp:
					deathdt = temp["deathDate"]
					divdate = res["divorce"]
					if divdate > deathdt:
						
			#newdate1 = time.strptime(marr, "%d/%m/%Y")
			#newdate2 = time.strptime(divv, "%d/%m/%Y")
			#if marr > divv:
			
						print "Divroce Date and Death Date for Individual ID",temp["ID"],"is not correct","\n"
					else:
						print "Divorce Date and Death Date for Individual ID",temp["ID"],"is correct","\n"

	
		



	
	
if __name__ == '__main__':
    marrbeforedeath = check_marriagebeforedeath()
	

			
