import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#DB Connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

#Check in family record Wife and Husband ids are not the same.
def check_unique_husband_wife(id):
	family = db.family.find({"FAMID" : id})
	flag = 0
	for doc in family:
		if (doc["WIFE"] != doc["HUSBAND"]):
			flag = 1
		else:
			flag = 0

	return flag

def main(n):
	unique_husband_wife = check_unique_husband_wife(n)
	print(unique_husband_wife)

if __name__ == '__main__':
    if len(sys.argv) > 1:
       	main(str(sys.argv[1]))