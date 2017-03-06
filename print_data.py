from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re
import sys
from all_db_operations import *
from prettytable import PrettyTable

person_detail = PrettyTable()
family_detail = PrettyTable()

def save_invalid_people_for_print(id, user_story,message):
	file_for_invalid_people_record = open('file_for_invalid_people_record.txt', 'a')
	message_for_person = "Error:  INDIVIDUAL:", user_story, "INDIVIDUAL_ID :",id, message
	file_for_invalid_people_record.write(' '.join(message_for_person)+'\n')

def save_invalid_family_for_print (id, user_story, message):
	file_for_invalid_family_record = open('file_for_invalid_family_record.txt', 'a')
	message_for_family = "Error:  Family:", user_story, "Family_ID :",id, message
	#print(' '.join(message_for_family))
	file_for_invalid_family_record.write(' '.join(message_for_family)+'\n')

def print_individuals():
	person_detail.field_names = ["ID", "Name", "Gender","Birthday","Age","Alive","Death","Child","Spouse"]
	results_for_people = get_people()
	array_of_indi = []
	for res in results_for_people:
		person_details = []		
		person_details.append(res["ID"])
		person_details.append(res["NAME"])
		if "SEX" in res:
			person_details.append(res["SEX"])
		else:
			person_details.append("NA")
		if "birthday" in res:
			hbd = datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			if "deathDate" in res:
				deathDate = datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
				age_of_person = deathDate.year - hbd.year
				person_details.append(hbd)
				person_details.append(age_of_person)
				person_details.append(False)
				person_details.append(deathDate)
			else:
				age_of_person = datetime.now().year - hbd.year
				person_details.append(hbd)
				person_details.append(age_of_person)
				person_details.append(True)
				person_details.append("NA")
		else:
			person_details.append("NA")	
			if "deathDate" in res:
				person_details.append("NA")
				person_details.append("NA")
				person_details.append(True)
				deathDate = datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
				person_details.append(deathDate)
			else:
				person_details.append("NA")
				person_details.append("NA")
				person_details.append("NA")
				person_details.append("NA")

		if "FAMS" in res:
			family = get_family_details(res["FAMS"])
			for doc in family:
				if "CHILDREN" in doc:
					person_details.append(doc["CHILDREN"])
				else:
					person_details.append("NA")
				if "HUSBAND" in doc:
					person_details.append(doc["HUSBAND"])
				else:
					person_details.append("NA")
		else:
			person_details.append("NA")
			person_details.append("NA")

		array_of_indi.append(person_details)
		list_of_person = filter(None, array_of_indi)
	for i in list_of_person:
		person_detail.add_row(i)
	return person_detail

def print_families():
	family_detail.field_names = ["ID", "Married", "Divorced","Husband Id","Husband Name","Wife ID","Wife Name","Children"]
	results_for_family = get_family()
	array_of_family = []
	for res1 in results_for_family:
		family_details = []
		family_details.append(res1["FAMID"])
		if "marriage" in res1:
			family_details.append(datetime.strptime(res1["marriage"],"%Y-%m-%d %H:%M:%S"))
		else:
			family_details.append("NA")
		if "divorce" in res1:
			family_details.append(datetime.strptime(res1["divorce"],"%Y-%m-%d %H:%M:%S"))
		else:
			family_details.append("NA")
		if "HUSBAND" in res1: 
			family_details.append(res1["HUSBAND"])
			result_for_husband = get_person_details(res1["HUSBAND"])
			for doc in result_for_husband:
				family_details.append(doc["NAME"])

		else:
			family_details.append("NA")
			family_details.append("NA")
		if "WIFE" in res1: 
			family_details.append(res1["WIFE"])
			result_for_wife = get_person_details(res1["WIFE"])
			for doc1 in result_for_wife:
				family_details.append(doc1["NAME"])
		else:
			family_details.append("NA")
			family_details.append("NA")

		
		if "CHILDREN" in res1:
			family_details.append(res1["CHILDREN"])
			
		else:
			family_details.append("NA")
		
		array_of_family.append(family_details)
		list_of_family = filter(None, array_of_family)
	for j in list_of_family:
		family_detail.add_row(j)
	return family_detail