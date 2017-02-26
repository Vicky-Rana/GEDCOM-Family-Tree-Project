"""
Marriage Before Death
"""
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
print("Database Connected!!")

def getChildrenList(id):
    family=db.family.find({"FAMID":id})
    for doc in family:
        try:
    return family


def main(n):
    print("START")
    childrens=getChildrenList(id)
    pprint(childrens)

if __name__ == '__main__':
    main("@F1@")
    # if len(sys.argv) > 1:
    #     print("START")
    #     main("@F1@")
    #    	#main(str(sys.argv[1]))
        