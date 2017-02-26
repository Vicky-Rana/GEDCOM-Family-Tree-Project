"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""
from .gedClasses import gedcomTagLine, individualPerson, familyClass
from datetime import datetime
from itertools import islice


def GEDCOMParser(filename):
    individual = []
    family = []
    gedlist = []
    filterGEDCOM = open("filterGEDCOM.txt", 'w')
    # readas a line from file and strip \n from the end
    lines = [line.rstrip('\n\r') for line in open(filename)]
    
    # Create and add  objects to the list
    for line in lines:
        current = gedcomTagLine(line)
        gedlist.append(current)
       
    #Following Loop to filter out relevent information and store it in a file
    for l in gedlist:
        if(l.tag!=None):
            filterGEDCOM.write(str(l.level)+"   "+str(l.tag)+"   "+str(l.ref)+"   "+str(l.arg)+"\n")
    # Check Every Tag
    for index, gedcomline in enumerate(gedlist):
        #for an Individual 
        if gedcomline.tag == 'INDI':

            date_type = None
            indiObject = {}
            indiObject["ID"] = str(gedcomline.ref)
            # set the object attributes untill next level 0
            for gedline in gedlist[index+1:]:
                
                if gedline.level == 0:
                    break
                if gedline.tag == "NAME":
                    indiObject["NAME"] = gedline.arg
                if gedline.tag == "SEX":
                    indiObject["SEX"] = gedline.arg[0]
                if gedline.tag == "BIRT":
                    date_type = "BIRT"
                if gedline.tag == "DEAT":
                    date_type = "DEAT"
                if gedline.tag == "FAMC":
                    indiObject["FAMC"] = gedline.arg[0]
                if gedline.tag == "FAMS":
                    indiObject["FAMS"]  = gedline.arg[0]

                # check if date is birth or date
                if gedline.tag == 'DATE':
                    if date_type == 'BIRT':
                        indiObject["birthday"] = str(datetime(
                            int(gedline.arg[2]),
                            int(datetime.strptime(gedline.arg[1], '%b').month),
                            int(gedline.arg[0]))
                        )
                        date_type = None
                    elif date_type == 'DEAT':
                        indiObject["deathDate"] = str(datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0]))
                        )
                        date_type = None

            # add object into the individual list
            #print("*****************")
            #print(indiObject)
            individual.append(indiObject)

        # For family list
        if gedcomline.tag == 'FAM':

            date_type = None
            familyObject = {}
            familyObject["FAMID"] = str(gedcomline.ref)
            # create blank object
            # ste values until next level 0
            children = []
            for gedline in gedlist[index + 1:]:
                if gedline.level == 0:
                    break
                if gedline.tag == "MARR":
                    date_type = "MARR"
                if gedline.tag == "DIV":
                    date_type = "DIV"
                if gedline.tag == "HUSB":
                    familyObject["HUSBAND"] = gedline.arg[0]
                if gedline.tag == "WIFE":
                    familyObject["WIFE"] = gedline.arg[0]
                if gedline.tag == "CHIL":
                    children.append(gedline.arg[0])
                    familyObject['CHILDREN'] = children
                if gedline.tag == "DATE": # check if marriage date 
                    if date_type == "MARR": # check if divorce date
                        familyObject["marriage"] = str(datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])))
                        date_type = None
                    elif date_type == "DIV":
                        familyObject.divorce = str(datetime(
                            int(gedline.arg[2]),
                            datetime.strptime(gedline.arg[1], '%b').month,
                            int(gedline.arg[0])))
                        date_type = None
            family.append(familyObject)

    return individual, family