from all_db_operations import *
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']


def US07_lessThan150():
	userStoryName('US07')
	#return_flag=False
	people=db.people.find({})
	results = [res for res in people] #count = cursor.count()
	people.close()
	#ageLessThan150=[]
	ageGreaterThan150=[]
	for res in results: 
		
		if "deathDate" in res  and "birthday" in res:
			
			death_date= datetime.strptime(res["deathDate"],"%Y-%m-%d %H:%M:%S")
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			
			difference_in_years = relativedelta(death_date, birthday).years
			
			if death_date.year -birthday.year >150:
				ageGreaterThan150.append(res['ID'])
	for personID in ageGreaterThan150:
		#person=get_person_details(personID)
		#print(personID)
		message="Person with "+personID+"has age greater than 150"
		save_invalid_people_for_print(personID,"US07",message)

    