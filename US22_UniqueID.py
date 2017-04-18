#from collections import counter
from print_data import *
#from dateutil.relativedelta import relativedelta
#Default File Path
# MongoDB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
# Check family present for particular individual



def unique_indids():
	userStoryName('US22')
	individual_list = []

	
	temp1 = []

	individual = get_people()
	
	for res in individual:
		
		if res["ID"] in individual_list:
			
			temp1.append(res["ID"])
			#message = "Individual ID"+str(id)+", occurs twice ,therefore it is not valid."
			#save_invalid_people_for_print(res["ID"], "US22", message)
		else:
			individual_list.append(res["ID"])
	
	
	unq_list = list(set(temp1))
	for i in unq_list:
		message = "Individual ID "+i+" , occurs twice ,therefore it is not valid."
		save_invalid_people_for_print(i, "US22", message)




	
def unique_famids():
	temp2=[]		
	family_list = []
	
	fam = get_family()
	for rest in fam:
		if rest["FAMID"] in family_list:
			idf=rest["FAMID"]
			temp2.append(rest["FAMID"])
			#message = "Family ID"+str(idf)+", occurs twice ,therefore it is not valid."
			#save_invalid_family_for_print(res["FAMID"], "US22", message)
		else:
			family_list.append(rest["FAMID"])
			
	unq_list1 = list(set(temp2))
	for i in unq_list1:
		message = "Family ID "+i+" , occurs twice ,therefore it is not valid."
		save_invalid_family_for_print(i, "US22", message)




	
