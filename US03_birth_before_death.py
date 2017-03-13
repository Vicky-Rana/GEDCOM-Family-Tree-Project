"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-03 Birth Before Date 
"""

from dateutil.relativedelta import relativedelta

from print_data import *


def birth_before_death():
    userStoryName('US03')
	return_flag=False
	results_for_people = get_people()
	
	for res in results_for_people:			
		if "deathDate" in res  and "birthday" in res:
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			difference_in_years = relativedelta(death_date, birthday).years
			difference= death_date.year - birthday.year
			if(difference > 0):
				return_flag=True
			else:
				return_flag=False
                message = "Birth Date is invalid for " + res["ID"] + " Please validate the birth Date."
				save_invalid_people_for_print(res["ID"], "US03", message)