"""
US33
"""
# import sys
from all_db_operations import *
from print_data import *

connection=MongoClient('localhost',27017)
db=connection['GEDCOMDB']


def getPeopleById(PersonId):
    results_for_people=get_people()
    for people in results_for_people:
        if people['ID'] == PersonId:
            return people


def US33_listOrphans():
    userStoryName('US33- List of Orphan Children')
    output('\t' + 'FAMILY ID' + '\t' + 'INDIVIDUAL ID' + '\t\t' + 'NAME')
    results_for_family = get_family()
    for family in results_for_family:
        if 'CHILDREN' not in family:
            continue
        husband = getPeopleById(family['HUSBAND'])
        wife = getPeopleById(family['WIFE'])
        if 'deathDate' in husband and 'deathDate' in wife:
            for child in family['CHILDREN']:
                child_name = getPeopleById(child)
                output('\t' + family['FAMID'] + '\t\t' + child + '\t\t\t' + child_name["NAME"][0] + " " + (child_name["NAME"][1]).strip("/"))


US33_listOrphans()
