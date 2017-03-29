from dateutil.relativedelta import relativedelta
from print_data import *
from src.gedParser import GEDCOMParser
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def US42_rejectIllegitimateDates():
    userStoryName('US42')
    families=get_family()
    allpeople=get_people()
    for res in allpeople:

        if 'birthday' in res and res["birthday"] is None:
            message="Invalid BirthDate Entered"

            save_invalid_people_for_print(res["ID"], "US42", message)
        if 'deathDate' in res and res["deathDate"] is None:
            message = "Invalid Death Date Entered"
            save_invalid_people_for_print(res["ID"], "US42", message)

    for res in families:
        if "marriage" in res and res["marriage"] is None:
            message = "Invalid marriage Date Entered"
            save_invalid_family_for_print(res["FAMID"], "US42", message)
        if 'divorce' in res and res["divorce"] is None:
            message = "Invalid divorce Date Entered"
            save_invalid_family_for_print(res["FAMID"], "US42", message)

US42_rejectIllegitimateDates()