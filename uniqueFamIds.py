import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#DB Connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

# Check only one family present with particular family id  
def check_distinct_Family(id):
	fam_list = db.family.distinct('_id',{"FAMID" : id})
	#Check number of families with same Family ID
	if len(fam_list) == 1:
		return "true"
	else:
		return "false"

def main(n):
    family_list = check_distinct_Family(n)
    print(family_list)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(str(sys.argv[1]))

