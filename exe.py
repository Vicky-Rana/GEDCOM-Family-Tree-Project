"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""
import argparse
import os
from prettytable import PrettyTable
from src.gedParser import GEDCOMParser
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#Default File Path

FILENAME = 'gedcom_files/myFTree.ged'

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
print(db)
print(pymongo.version)

people = db.people
family = db.family
#individual_id = people.insert_one(indi_hash).inserted_id
#cursor = people.find({})
#for document in cursor: 
#pprint("***********")
#pprint(document)
#data = open("My-Family-12-Feb-2017-425.ged").readlines()
#print(data)



p1 = PrettyTable()
p2 = PrettyTable()


#This is the function to print the family and individual details in a pretty table
def printPretty(individual, families):
    for i in individual:
        individual = people.insert_one(i)
    
    print('\n\t\t\t-----------------------------------------------------')
    print('\n\t\t\t\t\tINDIVIDUAL DETAILS ')
    print('\n\t\t\t-----------------------------------------------------')
    cursor = people.find({})
    for document in cursor: 
        pprint(document)


    for j in families:
        print(j)
        family_id = family.insert_one(j)

    print('\n\t\t\t-----------------------------------------------------')
    print('\n\t\t\t\t\tFAMILY DETAILS ')
    print('\n\t\t\t-----------------------------------------------------')
        
    cursor2 = family.find({})
    for document2 in cursor2: 
        pprint(document2)


# Main Funciton 
def main():
    
    parser = argparse.ArgumentParser() # Allow for args to be passed for filename
    action = parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME,
                        help="Specify file name" + FILENAME)

    args = parser.parse_args()
    path = args.file
    if os.path.exists(path):
        print("PATH VERIFIED...")
        individual, families = GEDCOMParser(path)
    else:
        print("[!!] FILE \"%s\" DOESN'T EXISIT.\n Terminiating..." % path)
        exit(-1)
    #printing values
    printPretty(individual, families)

if __name__ == '__main__':
    main()