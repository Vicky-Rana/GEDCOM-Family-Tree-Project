from print_data import *

def US32_multiple_births():
	userStoryName('US32')
	people = get_people()
	birth_dates = {}
	flipped = {}
	for doc in people:
		if "birthday" in doc and doc['birthday'] is not None:
			birth_date = datetime.date(datetime.strptime(doc["birthday"],"%Y-%m-%d %H:%M:%S"))
			birth_dates[doc["ID"]] = birth_date
	#print(birth_dates) 

	for key, value in birth_dates.items():
		if value not in flipped:
			flipped[value] = [key]
		else:
			flipped[value].append(key)

	for key, value in flipped.items():
		if (len(value) > 1):
			#print("This is the birth date",key)
			#print("This is ids of individual", value)
			k=key
			b=value
			message="Individual with ID" + str(value) + "have same birthdate:  " + str(key)
			#print(message) 
			output('\t'+message)
def main():
	US32_multiple_births()

if __name__ == "__main__":
    main()