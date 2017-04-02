"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-39 List Upcoming Anniversary 

"""
#from collections import counter
from print_data import *

def getPeopleById(PersonId):
    results_for_people=get_people()
    for people in results_for_people:
        if people['ID'] == PersonId:
            return people

def upcoming_anniversary():
	userStoryName('US39-List of Upcoming Anniversaries')
	output('\t' + 'HUSBAND' + '\t\t\t\t' + 'WIFE' + '\t\t\t\t' + 'ANNIVERSARY DATE')
	return_flag=False
	results_for_family = get_family()
	current=datetime.now()
	
	for res in results_for_family: 
			
		if "marriage" in res and res["marriage"] is not None:
			anniversary= datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
			if (anniversary.month- current.month   > 0 ):
				return_flag=True
				husband= getPeopleById(res["HUSBAND"])
				wife= getPeopleById (res["WIFE"])

				h=husband["NAME"][0]+"  " +husband["NAME"][1].strip("/")
				w=wife["NAME"][0]+ " "+ wife["NAME"][1].strip("/")   
				ad=str(anniversary.day) + "/" + str(anniversary.month)
				output('\t' + str(h) + '\t\t'+ str(w) + '\t\t\t' + str(res["marriage"]))
							
			elif (anniversary.month- current.month==0 & anniversary.day - current.day >0):
				return_flag=True
				husband= getPeopleById(res["HUSBAND"])
				wife= getPeopleById (res["WIFE"])

				h=husband["NAME"][0]+"  " +husband["NAME"][1].strip("/")
				w=wife["NAME"][0]+ " "+ wife["NAME"][1].strip("/")   
				ad=str(anniversary.day) + "/" + str(anniversary.month)
				output('\t' + str(h) + '\t\t'+ str(w) + '\t\t\t' + str(res["marriage"]))

			else:
				return_flag=False
				
	return return_flag

