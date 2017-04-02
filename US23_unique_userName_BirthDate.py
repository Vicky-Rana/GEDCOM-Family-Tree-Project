"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-23List Unique Username and Birthdate

"""
from print_data import *

# Check family present for particular individual
def unique_name_bdate():
	userStoryName('US23')
	#Search for individual
	results_for_people = get_people()

	for res in results_for_people:
		
		id = res["ID"]
		for doc2 in results_for_people:
			date = doc2["birthday"]
			name = doc2["NAME"]
			idd = doc2["ID"]
					
			if(date==res["birthday"] and name==res["NAME"] and idd!=id ):
				number=[]
				number.append(id)
				for value in number:
					message="Individual with" +res["ID"]+ " doesn't have unique birthdate" 
					save_invalid_people_for_print(res["ID"], "US23", message)
 
	
	
 