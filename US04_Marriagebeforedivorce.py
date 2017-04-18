#from collections import counter
from print_data import *
#DB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']








def check_marriagebeforedivorce():
	userStoryName('US04')
	
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



	

	

			
