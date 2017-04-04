from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def US09_birth_before_death_of_parents():
	userStoryName('US09')
	family = get_family()
	valid_difference_mom_and_child = True
	for doc in family:
		if (("CHILDREN" in doc) and ("HUSBAND" in doc) and ("WIFE" in doc)):
			mom_deathDate = get_death_date(doc["WIFE"])
			dad_deathDate = get_death_date(doc["HUSBAND"])
			for child in doc["CHILDREN"]: 
				child_birthDate =  get_birth_date(child)
				if(child_birthDate != ""):
					valid_difference_mom_and_child = check_valid_birth_wrt_mom(mom_deathDate, child_birthDate)
					valid_difference_dad_and_child = check_valid_birth_wrt_dad(dad_deathDate, child_birthDate)
					if(valid_difference_mom_and_child == False or valid_difference_dad_and_child == False):
						output('\t'+doc["FAMID"] +'\t\t%-10s'+ str(child_birthDate) + '\t\t%-10s' % str(dad_deathDate) + '\t\t%-10s' % str(mom_deathDate))
				
def get_birth_date(individual):
	indi = get_person_details(individual)
	for doc in indi:
		if "birthday" in doc:
			birth_date = datetime.date(datetime.strptime(doc["birthday"],"%Y-%m-%d %H:%M:%S") )
		else:
			birth_date = ""
	return birth_date

def get_death_date(individual):
	indi = get_person_details(individual)
	for doc in indi:
		if "deathDate" in doc and doc['deathDate'] is not None:
			death_date = datetime.date(datetime.strptime(doc["deathDate"],"%Y-%m-%d %H:%M:%S") )
		else:
			death_date = ""
	return death_date

def check_valid_birth_wrt_mom(death_date, child_birthDate):
	if(death_date == ""):
		return True
	else:
		delta = death_date - child_birthDate
		if(int(delta.days/30.4) < 0):
			return False
		else:
			return True

def check_valid_birth_wrt_dad(death_date, child_birthDate):
	if(death_date == ""):
		return True
	else:
		delta = death_date - child_birthDate	
		if(int(delta.days/30.4) > -9 and int(delta.days/30.4) <= 0):
			return False
		else:
			return True

def main():
	US09_birth_before_death_of_parents()

if __name__ == "__main__":
    main()