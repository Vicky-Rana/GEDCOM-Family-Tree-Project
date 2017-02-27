"""
Marriage Before Death
"""
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime

#Datebase Connection
connection=MongoClient('localhost',27017)
db=connection['GEDCOMDB']

def getFamilyData(famID):
    family=db.family.find({"FAMID":famID})
    marriageDate=0
    flag=0
    for document in family:
        try:
            marriageDate=getMarriageDate(famID)
            marriageDate=marriageDate.split("-")
            deathData=getDeathDate(famID)
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
                return False
            else:
                return True 
        except:
            marriageDate="No marriage"
            deathData="no death"

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

def main(id):
    ans=getFamilyData(id)
    
    print(ans)

if __name__=='__main__':
    #main("@F5@")
    if len(sys.argv)>1:
        #print("START")
        main(str(sys.argv[1]))