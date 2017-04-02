"""
Sprint 1
Developed By : Abhilash Ugaonkar
User Story: US-01 List Upcoming Anniversary 

"""
#from collections import counter
from print_data import *

def dates_before_current_date():
    userStoryName('US01-Dates Before Current Date')
    return_flag=False
    results_for_family = get_family()
    results_for_people = get_people()
    current=datetime.now()

    for res in results_for_people:
        if "birthday" in res and res["birthday"]!=None:
            birthday= datetime.strptime(res["birthday"],"%Y-%m-%d %H:%M:%S")

            if (current.year-birthday.year == 0 ):
                if(current.month-birthday.month ==0):
                    if(current.day-birthday.day >  0):
                        message="Error!!! ...Birth Date is not before Current Date "
                        save_invalid_people_for_print(res["ID"], "US01", message)

    for res in results_for_family:
        if "marriage" in res and res["marriage"] is not None:
            anniversary= datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")

            if (current.year-anniversary.year  == 0 ):
                if (current.month-anniversary.month  == 0):
                    if(current.day-anniversary.day > 0):
                        message="Error!!! ...Marriage Date is not before Current Date "
                        save_invalid_family_for_print(res["FAMID"], "US01", message)

    for res in results_for_family:
        if "divorce" in res and res["divorce"] is not None:
            div= datetime.strptime(res["divorce"],"%Y-%m-%d %H:%M:%S")
            if (current.year-div.year == 0 ):
                if (current.month-div.month == 0):
                    if(current.day-div.day > 0):
                        message="Error!!! ...Divorce Date is not before Current Date "
                        save_invalid_family_for_print(res["FAMID"], "US01", message)

