from all_db_operations import *
from print_data import *

def US08_birth_before_marriage_of_parents():
	userStoryName('US08')
	diff = False
	family = get_family()
	for doc in family:
		if (("CHILDREN" in doc) and ("HUSBAND" in doc) and ("WIFE" in doc) and ("marriage" in doc)):
			for child in doc["CHILDREN"]:
				birthday = get_birth_date(child)
				marriage_date = datetime.date(datetime.strptime(doc["marriage"],"%Y-%m-%d %H:%M:%S"))
				if("divorce" in doc):
					marriage_date = datetime.date(datetime.strptime(doc["divorce"],"%Y-%m-%d %H:%M:%S"))
					diff = valid_difference_marriage_and_child(marriage_date,birthday)					
				else:
					diff = valid_difference_marriage_and_child(marriage_date,birthday)
				if(diff == True):
					output('\t'+doc["FAMID"] +'\t\t%-10s'+ str(birthday) + '\t\t%-10s' % str(marriage_date))

def get_birth_date(individual):
	indi = get_person_details(individual)
	for doc in indi:
		if "birthday" in doc:
			birth_date = datetime.date(datetime.strptime(doc["birthday"],"%Y-%m-%d %H:%M:%S") )
		else:
			birth_date = ""
	return birth_date


def valid_difference_marriage_and_child(marriage_date, child_birthDate):	
	delta = child_birthDate - marriage_date
	if ((int(delta.days/30.4)) < -9):
		return True
	else:
		return False

def main():
	US08_birth_before_marriage_of_parents()

if __name__ == "__main__":
    main()