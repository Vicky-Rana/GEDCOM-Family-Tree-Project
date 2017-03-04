import pymongo
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
people = db.people
family = db.family

def get_family():
	family=db.family.find({})
	results_for_family = [i for i in family] #count = cursor.count()
	family.close()
	return results_for_family

def get_people():
	people=db.people.find({})
	results_for_people = [j for j in people] #count = cursor.count()
	people.close()
	return results_for_people

def get_person_details(id):
	person = db.people.find({"ID" : id})
	result_for_person = [ptr for ptr in person]
	return result_for_person

def get_family_details(fam_id):
	family = db.family.find({"FAMID" : fam_id})
	result_for_family = [ptr2 for ptr2 in family]
	return result_for_family

def update_valid_person(id):
	person = db.people.update({"ID":id},{"$set":{"isValid":False}})
