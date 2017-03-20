"""
Sprint 2
Developed By : Abhilash Ugaonkar
User Story: US-36 List Recent Death 

"""
#from collections import counter
from print_data import *

def recent_deaths():
	userStoryName('US36-Recent Deaths')
	output('\t' + 'NAME' + '\t\t\t'+ 'DEATH DATE')
	return_flag=False
	results_for_people = get_people()
	current=datetime.now()
	
	for res in results_for_people: 			
		if "deathDate" in res:
			deathDay= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			if (current.year - deathDay.year == 0 ):
				if (current.month - deathDay.month ==0 and current.day-deathDay.day > 0):
					name=res["NAME"][0].strip("/") + ' ' + res["NAME"][1].strip("/")
					output('\t' + str(name) + '\t\t' + str(res["deathDate"]))

