"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""
import argparse
import os
from src.gedParser import GEDCOMParser
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
from US05_marriageBeforeDeath import *
from US07_lessThan150 import *
from US31_above30_single import * 
from US30_living_marriages import * 
from US02_birth_date_less_marriage_date import * 
from US39_upcoming_anniversary import *
from US23_unique_userName_BirthDate import *
from US03_birth_before_death import *
from all_db_operations import *
from print_data import *

FILENAME = 'gedcom_files/myTree.ged'

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
people = db.people
family = db.family
db.people.remove({})
db.family.remove({})
def printPretty(individual, families):
    for i in individual:
        individual = people.insert_one(i)

    for j in families:
        family_id = family.insert_one(j)

    # Call User story 05
    US05_marriageBeforeDeath()

    #Call User story 07
    US07_lessThan150()

    # Call Usere Story 30
    living_marriages()
    # Call User Story 02
    birth_date_less_marriage_date()
    #Call user story 31
    more_than_30_unmarried()
    
    # Call User story 39
    upcoming_anniversary()

    # User Story 23
    unique_name_bdate()

    # User Story 03
    birth_before_death()
    # Print Individual Data
    print(print_individuals())
    print(print_families())

def main():
    parser = argparse.ArgumentParser() # Allow for args to be passed for filename
    action = parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME,
                        help="Specify file name" + FILENAME)

    args = parser.parse_args()
    path = args.file
    if os.path.exists(path):
        #print("PATH VERIFIED...")
        individual, families = GEDCOMParser(path)
    else:
        print("[!!] FILE \"%s\" DOESN'T EXISIT.\n Terminiating..." % path)
        exit(-1)
    #printing values
    printPretty(individual, families)

if __name__ == '__main__':
    main()