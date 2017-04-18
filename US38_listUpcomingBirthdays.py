from all_db_operations import *
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']


def US38_listUpcomingBirthdays():
	userStoryName('US38')
	#return_flag=False
	people=db.people.find({})
	results = [res for res in people] 
	people.close()

	current=datetime.now()
	output('\t' + 'Individual ID' + '\t\t' + 'Name' + '\t\t\t\t' + 'Birthday')
	for res in results: 
			
		if "birthday" in res and res["birthday"] is not None:
			birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")
			if (birthday.month- current.month   > 0 ):
				output('\t' + res["ID"] + '\t\t\t%-10s' % res["NAME"][0] + " %-10s" % (res["NAME"][1]).strip("/") + '\t\t' + res['birthday'])

			if (birthday.month - current.month == 0 & birthday.day > current.day):
				output('\t' + res["ID"] + '\t\t' + res["NAME"][0] + " " + (res["NAME"][1]).strip("/") + '\t\t%30s' % res['birthday'])
