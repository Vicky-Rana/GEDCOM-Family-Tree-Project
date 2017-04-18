"""
Sprint 2
Developed By : Abhilash Ugaonkar
User Story: US-27 Include Individual Ages

"""
from datetime import datetime
from all_db_operations import *
from print_data import *

def individual_age():
	userStoryName('US27-Include Individual Ages')
	results_for_people = get_people()
	output('\t' + 'NAME' + '\t\t\t'+ 'AGE')
	for res in results_for_people:
		if "birthday" in res and res["birthday"] is not None:
			hbd = datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			if "deathDate" in res and res["deathDate"] is not None:
				deathDate = datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
				age_of_person = deathDate.year - hbd.year
				name=res["NAME"][0].strip("/") + ' ' + res["NAME"][1].strip("/")
				output('\t' + str(name) + '\t\t' + str(age_of_person))
			else:
				age_of_person = datetime.now().year - hbd.year
				name=res["NAME"][0].strip("/") + ' ' + res["NAME"][1].strip("/")
				output('\t' + str(name) + '\t\t' + str(age_of_person))

			