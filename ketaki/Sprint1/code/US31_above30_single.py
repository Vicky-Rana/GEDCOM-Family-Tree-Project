from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']


def more_than_30_unmarried():

	family=db.family.find({})
	results_for_family = [i for i in family] #count = cursor.count()
	family.close()
	array_of_husband_and_wife = []


	people=db.people.find({})
	results_for_people = [j for j in people] #count = cursor.count()
	people.close()
	array_of_people= []
	total_people_above_30_not_married = 0;

	for res in results_for_family: 
		if "HUSBAND" in res and "WIFE" in res:
			array_of_husband_and_wife.append(res["HUSBAND"])
			array_of_husband_and_wife.append(res["WIFE"])
	all_married_people = list(set(array_of_husband_and_wife))
	for res1 in results_for_people: 
		array_of_people.append(res1["ID"])
	all_people = list(set(array_of_people))
	
	unmarried_people = set(all_people) - set(all_married_people)
	for k in unmarried_people:
		person = db.people.find({"ID" : k})
		result_for_person = [ptr for ptr in person]
		for details in result_for_person:
			age_of_person = 0	
			if "birthday" in details:
				hbd = datetime.strptime(details["birthday"],"%Y-%m-%d %H:%M:%S")
				age_of_person = datetime.now().year - hbd.year
				if age_of_person > 30:
					print(details["ID"])
					total_people_above_30_not_married = total_people_above_30_not_married +1
	print("total No of people above 30 and not married", total_people_above_30_not_married)


if __name__ == '__main__':
    check_birth_before_marriage = more_than_30_unmarried()
   