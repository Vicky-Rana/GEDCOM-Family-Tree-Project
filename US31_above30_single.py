from print_data import *

def more_than_30_unmarried():
    userStoryName('US31')
	results_for_family = get_family()
	results_for_people = get_people()
	array_of_husband_and_wife = []
	array_of_people =[]
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
		result_for_person = get_person_details(k)
		for details in result_for_person:
			if "birthday" in details and "deathDate" not in details:
				age_of_person = 0
				hbd = datetime.strptime(details["birthday"],"%Y-%m-%d %H:%M:%S")
				age_of_person = datetime.now().year - hbd.year
				if age_of_person > 30:
					message = "age is " + str(age_of_person) + " not married yet."
					save_invalid_people_for_print(details["ID"], "US31", message)