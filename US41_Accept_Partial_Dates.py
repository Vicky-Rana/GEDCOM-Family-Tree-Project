"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-01 List Upcoming Anniversary 

"""
#from collections import counter
from print_data import *

def US41_accpet_partial_dates():
    userStoryName('US41-Include Partial Dates')
    return_flag=False
    results_for_family = get_family()
    results_for_people = get_people()

    for res in results_for_people:
        if "birthday" in res and res["birthday"]==None:
            print(str(res["ID"])+ " Has Partial Date in GEDCOM File..")
            message="Error!!! ..."+str(res["ID"])+ " Has Partial Birthdate in GEDCOM File." 
            output('\t'+message)

    for res in results_for_family:
        if "marriage" in res and res["marriage"] == None:           
            message= "Error!!! ..."+str(res["FAMID"])+ " Has Partial Marriage Date in GEDCOM File." 
            output('\t'+message)

    for res in results_for_family:
        if "divorce" in res and res["divorce"] == None:
            message="Error!!! ..."+str(res["ID"])+ " Has Partial Divorce Date in GEDCOM File." 
            output('\t'+message)

def main():
    US41_accpet_partial_dates()

if __name__ == "__main__":
    main()