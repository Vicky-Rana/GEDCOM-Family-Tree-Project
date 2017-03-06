"""
Marriage Before Death
"""
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
from print_data import *
from all_db_operations import *
import datetime

#Datebase Connection
connection=MongoClient('localhost',27017)
db=connection['GEDCOMDB']

def getFamilyData():
    family=db.family.find({})
    
    marriageDate=0
    flag=0
    for document in family:
        try:
            famID=document["FAMID"]
            marriageDate=getMarriageDate(famID)
            marriageDate=marriageDate.split("-")
            deathData=getDeathDate(famID)
            marriageAfterDeath=[]
            marriageBeforeDeath=[]
            for death in deathData:
                death=death.split("-")
                if death[0]<marriageDate[0]:
                    flag=0
                elif death[0]==marriageDate[0]:
                    if death[1]<marriageDate[0]:
                        flag=0
                    elif death[1]==marriageDate[1]:
                        if death[2]<marriageDate[2]:
                            flag=0
                        else:
                            
                            flag=1
                    else:
                        
                        flag=1
                else:
                    
                    flag=1
            if(flag==0):
                #return False
                
                marriageAfterDeath.append(famID)
            else:
                #return True 
                marriageBeforeDeath.append(famID)
            
            for familyID in marriageAfterDeath:
                message="A member of this family has marriage date after their death date"
                save_invalid_family_for_print(familyID,"US05",message)
        except:
            marriageDate="No marriage"
            deathData="No Death"

def getMarriageDate(id):
    family=db.family.find({"FAMID":id})
    for document in family:
        try:
            marriage_date=document["marriage"]
        except:
            continue
    marriage_date=marriage_date.split(" ")
    return marriage_date[0]

def getDeathDate(id):
    people=db.people.find({"FAMS":id})
    peoples=list()
    for document in people:
        try:
            death=document["deathDate"]
            death=death.split(" ")
            peoples.append(death[0])
        except:continue
    return peoples


getFamilyData()