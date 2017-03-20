from all_db_operations import *
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def US35_list_recent_births():
	userStoryName('US35')
	people = get_people()
	for doc in people:
		if "birthday" in doc:
			birth_date = datetime.strptime(doc["birthday"],"%Y-%m-%d %H:%M:%S") 
			delta = datetime.date(datetime.now()) - datetime.date(birth_date)
			if(delta.days < 30 and delta.days >= 0):
				output('\t' + doc["ID"] + '\t\t\t%-10s' % doc["NAME"][0] + " %-10s" % (doc["NAME"][1]).strip("/") + '\t\t' + doc['birthday'] + '\t\t' + str(delta.days))

	