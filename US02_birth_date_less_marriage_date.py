#from collections import counter
from print_data import *


def birth_date_less_marriage_date():
	userStoryName('US02')
	results = get_family()
	for res in results:
		if "marriage" in res and res["marriage"] is not None:
			wife_age = 0
			husband_age = 0
			marriage_date = datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
			if "HUSBAND" in res and "WIFE" in res:
				result_for_husband = get_person_details(res["HUSBAND"])
				result_for_wife = get_person_details(res["WIFE"])
				for doc in result_for_husband:
					if doc["birthday"] is not None:
						hbd = datetime.strptime(doc["birthday"],"%Y-%m-%d %H:%M:%S")
						husband_age = marriage_date.year - hbd.year
				for doc1 in result_for_wife:
					if doc1["birthday"] is not None:
						wbd = datetime.strptime(doc1["birthday"],"%Y-%m-%d %H:%M:%S")
						wife_age = marriage_date.year - wbd.year
				if wife_age < 18 or husband_age < 18:
					message = "Age of Wife is "+str(wife_age)+", Age of Husband is "+str(husband_age)+ ", therefore marriage is not valid."
					save_invalid_family_for_print(res["FAMID"], "US02", message)