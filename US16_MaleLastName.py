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
def male_last_names():
    userStoryName('US16')
    """ US16 -- all males in a family should have the same last name """
    #anom_type = "US16"
    #return_flag = True
    families = get_family()

    for family in families:
        males = []
        if 'HUSBAND' in family or 'CHILDREN' in family:
            #print(family['FAMID'])
            males.append(getPeopleById(family['HUSBAND'])['NAME'])
            if 'CHILDREN' in family:
                for child in family['CHILDREN']:
                    #print child
                    child_data=getPeopleById(child)
                    if 'SEX' in child_data:
                        if child_data['SEX']=='M':
                            males.append(child_data['NAME'])
        unique_surname=set()
        for male in males:
            unique_surname.add(male[1].strip('/'))
            #print male[1].strip('/')
            
        if len(unique_surname)>1:
            message = "Last names of all the males in this Family is not Unique"
            save_invalid_family_for_print(family["FAMID"], "US16", message)
                
    
if __name__ == '__main__':
    male_last_names()

    

    
