"""
Following is the User Story to check if a family has less than 5 kids born on same day
"""
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#DB connection
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def getChildrenList(id):
    #print(id)
    family = db.family.find({"FAMID" : id})
    flag = 0
    for doc in family:
        try:c=doc["CHILDREN"]
        except:c=False
        if(c!=False):birthdays=getBirthday(c)
        #print(type(birthdays))
        if(c==False):
            return True
        if(len(birthdays.values())==1):
            return True
        elif(len(birthdays.values())<=5 and len(birthdays.values())>len(set(birthdays.values()))):
            return True
        else:
            return False
            

def getBirthday(c):
    people=db.people.find({})
   
    results = [res for res in people]
    people.close()
    idAndBirthday=dict()
    for all in c:
        for res in results:
            
            if res["ID"] == all:
                idAndBirthday[all]=res["birthday"]
                
                break
    return idAndBirthday
def main(n):
    a=getChildrenList(n)
 


if __name__ == '__main__':
    if len(sys.argv) > 1:
       	main(str(sys.argv[1]))
 