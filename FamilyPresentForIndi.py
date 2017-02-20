import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#Default File Path
# MongoDB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
# Check family present for particular individual
def check_family_present_for_individual(id):
	flag = 0
	#Search for individual
	individual = db.people.find({"ID" : id})
	for doc in individual:
		#Check for family
		family = db.family.find({"FAMID" : doc["FAMS"]})
		#print(family)
		if family:
			#If family present return 1
			flag = 1
		else:
			# If family not present return 0
			flag = 0
	return flag

def main(n):
    family_present = check_family_present_for_individual(n)
    print(family_present)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(str(sys.argv[1]))

