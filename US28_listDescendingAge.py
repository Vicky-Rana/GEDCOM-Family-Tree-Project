from datetime import date

from print_data import *


def getPeopleById(PersonId):
    results_for_people = get_people()
    for people in results_for_people:
        if people['ID'] == PersonId:
            return people


def US28_listDescendingAge():
    userStoryName('US28-listDescendingAge')
    output('\t' + 'FAM_ID' + '\t\t' + 'ID' + '\t\t\t' + 'AGE')
    familyInfo = get_family()
    for fam in familyInfo:
        age = list()
        if 'CHILDREN' in fam:
            # print fam['FAMID']
            # print"-------------"
            for child in fam['CHILDREN']:
                # print child
                child_info = getPeopleById(child)
                if 'birthday' in child_info and child_info['birthday'] is not None:

                    birthday = datetime.strptime(child_info["birthday"], "%Y-%m-%d %H:%M:%S")
                    if 'deathDate' in child_info and child_info['deathDate'] is not None:
                        death_date = datetime.strptime(child_info["deathDate"], "%Y-%m-%d %H:%M:%S")
                        age.append([abs(death_date.year - birthday.year), child])
                    else:

                        age.append([abs(date.today().year - birthday.year), child])

            # print age
            # age=sorted(age,reverse=True)
            # print age
            # print"-------------"
            output('\t' + fam['FAMID'])
            for child_age in age:
                output('\t\t\t\t' + str(child_age[1]) + "\t\t" + str(child_age[0]))
            output('\t---------------------------')


US28_listDescendingAge()
