"""
US_14
"""
from all_db_operations import *
from print_data import *

connection=MongoClient('localhost',27017)
db=connection['GEDCOMDB']
def getPeopleById(id):
    results_for_people=get_people()
    for people in results_for_people:
        if people['ID']==id:
            return people
def US14_multipleBirthLessThan5():
    userStoryName('US14')
    results_for_family=get_family()
    results_for_people=get_people()
    for family in results_for_family:
        if 'CHILDREN' not in family:
            continue
        if len(family['CHILDREN'])>5:
            print(family['CHILDREN'])
            s=set()
            for children in family['CHILDREN']:
                person=getPeopleById(children)
                s.add(person['birthday'])
            if len(s)==1:
                message="More Than 5 Children born on same day/same time in this family"
                save_invalid_family_for_print(family['FAMID'],"US14",message)
                # US14_multipleBirthLessThan5()
