"""
US33
"""
from all_db_operations import *
from print_data import *

connection=MongoClient('localhost',27017)
db=connection['GEDCOMDB']
def US29_listDeceased():
    userStoryName('US29 - List of Deceased People')
    output('\t' + 'People ID' + '\t\t' + 'Name' + '    \t\t' + 'Death Date')
    results_for_people=get_people()
    for people in results_for_people:
        if 'deathDate' in people:
            death = people['deathDate'].split(' ')
            output('\t' + people['ID'] + "\t\t" + people["NAME"][0] + " " + (people["NAME"][1]).strip("/") + "    \t\t" +death[0])
