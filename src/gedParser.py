"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""
from .gedClasses import gedcomTagLine, individualPerson, familyClass
from datetime import date
from datetime import datetime


def GEDCOMParser(filename):
    individual = []
    family = []
    gedlist = []

    # readas a line from file and strip \n from the end
    lines = [line.rstrip('\n\r') for line in open(filename)]

    # Create and add  objects to the list
    for line in lines:
        current = gedcomTagLine(line)
        gedlist.append(current)

    # Check Every Tag
    for index, gedcomline in enumerate(gedlist):
        #for an Individual 
        if gedcomline.tag == 'INDI':

            date_type = None
            indiObject = individualPerson(gedcomline.ref)

            # set the object attributes untill next level 0
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "NAME":
                    indiObject.name = gedline.arg
                if gedline.tag == "SEX":
                    indiObject.sex = gedline.arg[0]
                if gedline.tag == "BIRT":
                    date_type = "BIRT"
                if gedline.tag == "DEAT":
                    date_type = "DEAT"
                if gedline.tag == "FAMC":
                    indiObject.famc.append(gedline.arg[0])
                if gedline.tag == "FAMS":
                    indiObject.fams.append(gedline.arg[0])

                # check if date is birth or date
                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        indiObject.birthday = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None
                    elif date_type == 'DEAT':
                        indiObject.deathDate = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])
                        )
                        date_type = None

            # add object into the individual list
            individual.append(indiObject)

        # For family list
        if gedcomline.tag == 'FAM':

            date_type = None

            # create blank object
            familyObject = familyClass(gedcomline.ref)

            # ste values until next level 0
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject.husband = gedline.arg[0]
                if gedline.tag == "WIFE":
                    familyObject.wife = gedline.arg[0]
                if gedline.tag == "CHIL":
                    familyObject.children.append(gedline.arg[0])

                
                if gedline.tag == "DATE": # check if marriage date 
                    if date_type == "MARR": # check if divorce date

                        familyObject.marriage = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None

                    elif date_type == "DIV":

                        familyObject.divorce = date(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        date_type = None
            
            family.append(familyObject)

    return individual, family