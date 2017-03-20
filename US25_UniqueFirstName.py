from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
#from collections import counter
import re
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
from all_db_operations import *
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def getPeopleById(PersonId):
    results_for_people=get_people()
    for people in results_for_people:
        if people['ID'] == PersonId:
            return people
def unique_first_famnames():
    userStoryName('US25')
    """ US25 -- all childrens in a family should not have the same first name """
    
    families = get_family()

    for family in families:
        males = []
        if 'HUSBAND' in family or 'CHILDREN' in family:
            #print(family['FAMID'])
            males.append(getPeopleById(family['HUSBAND'])['NAME'])
            #males.append(getPeopleById(family['WIFE'])['NAME'])
            
            if 'CHILDREN' in family:
                for child in family['CHILDREN']:
                    #print child
                    child_data=getPeopleById(child)
                    #if 'SEX' in child_data:
                    #    if child_data['SEX']=='M':
                    males.append(child_data['NAME'])
        unique_surname=list()
        for male in males:
            unique_surname.append(male[0])
            #print unique_surname
            #print male[0]
        
        if len(unique_surname) != len(set(unique_surname)):
        #if len(unique_surname[1])>1:
            #print "Unique"
            message = "First name of some members in this Family is Unique"
            save_invalid_family_for_print(family["FAMID"], "US25", message)
                
    
if __name__ == '__main__':
    unique_first_famnames()
