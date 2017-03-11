"""
US33
"""
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
#from print_data import *
from all_db_operations import *
import datetime

connection=MongoClient('localhost',27017)
db=connection['GEDCOMDB']
print('connected')

def US14_multipleBirthLessThan5():
    print("inside function")
    results_for_family=get_family()
    results_for_people=get_people()
    for family in results_for_family:
        if 'CHILDREN' not in family:
            continue
        print(family['CHILDREN'])
        



US14_multipleBirthLessThan5()