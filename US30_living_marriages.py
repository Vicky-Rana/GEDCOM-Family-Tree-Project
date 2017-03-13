#from collections import counter
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
people = db.people
family = db.family

existing_living_marriages = []
def living_marriages():
	userStoryName('US30')
	results = get_family()
	for res in results: 
		#print(res)
		wife_age = 0
		husband_age = 0
		
		if "marriage" in res:
			marriage_date = datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
			if "HUSBAND" in res and "WIFE" in res: 
				result_for_husband = get_person_details(res["HUSBAND"])
				result_for_wife = get_person_details(res["WIFE"])
				husband_alive = True
				wife_alive = True
				for doc in result_for_husband:
					if "deathDate" in doc:
						husband_alive = False
				for doc1 in result_for_wife:
					if "deathDate" in doc1:
						wife_alive = False
				if wife_alive != True and husband_alive != True:
					existing_living_marriages.append(res["FAMID"])
	unq_marriages = list(set(existing_living_marriages))
	for i in unq_marriages:
		find_family(i)

def find_family(FAMID):
	family = get_family_details(FAMID)
	for doc1 in family:
		message = "This is no Living Marriage as " + doc1["HUSBAND"] + " and " + doc1["WIFE"] + " one of them is not alive"
		save_invalid_family_for_print(FAMID, "US30", message)