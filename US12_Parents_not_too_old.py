from all_db_operations import *
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def US12_Parents_not_too_old():
	userStoryName('US12')
	people = get_people()
	family = get_family()

	for doc in family:
		if "CHILDREN" in doc:
			age_of_mother = age_of_person(doc["WIFE"])
			age_of_father = age_of_person(doc["HUSBAND"])
			array_of_age_of_children  = age_of_children(doc["CHILDREN"])
			for child_age in array_of_age_of_children:
				if(((age_of_mother - child_age) >= 60) or ((age_of_father - child_age) >= 80)):
					age_differnece_with_mother = "difference between mother and children age " + str(age_of_mother - child_age)
					age_differnece_with_father = "difference between father and children age " + str(age_of_father - child_age)
					output('\t' + doc["FAMID"] + '\t\t\t%-10s' % doc["WIFE"] + " %-10s" % doc["HUSBAND"] + '\t\t' + age_differnece_with_mother + '\t\t' + age_differnece_with_father)
                   
			



def age_of_person(person):
	person_details = get_person_details(person)
	for doc1 in person_details:
		if "birthday" in doc1 and doc1["birthday"] is not None:
			delta = datetime.date(datetime.now()) - datetime.date(datetime.strptime(doc1["birthday"],"%Y-%m-%d %H:%M:%S"))
			return int(delta.days/365.25)
		else:
			return -1

def age_of_children(children):
	array_of_children_ages = []
	for child in children:
		child_info = get_person_details(child)
		for doc2 in child_info:
			if "birthday" in doc2:
				delta = datetime.date(datetime.now()) - datetime.date(datetime.strptime(doc2["birthday"],"%Y-%m-%d %H:%M:%S"))
				array_of_children_ages.append(int(delta.days/365.25))
			else:
				array_of_children_ages.append(-1)
	return array_of_children_ages