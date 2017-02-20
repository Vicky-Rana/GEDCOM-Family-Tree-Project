import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#DB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

# Check in family unique children ids present for each family
def check_childeren_list(id):
	#Search family	
	family = db.family.find({"FAMID" : id})
	flag = 0
	for doc in family:
		#Check unique children are present or not
		if len(doc["CHILDREN"]) == len(set(doc["CHILDREN"])) or (len(doc["CHILDREN"]) == 0):
			flag = 1
		else:
			flag = 0

	return flag

def main(n):
	children_list = check_childeren_list(n)

if __name__ == '__main__':
    if len(sys.argv) > 1:
       	main(str(sys.argv[1]))
