#from collections import counter
from print_data import *


def Marriage_after_14():
    userStoryName('US10')
    results = get_family()
    for res in results:
        if "marriage" in res and res["marriage"] is not None:
            wife_age = 0
            husband_age = 0
            marriage_date = datetime.strptime(res["marriage"],"%Y-%m-%d %H:%M:%S")
            if "HUSBAND" in res and "WIFE" in res:
                result_for_husband = get_person_details(res["HUSBAND"])
                result_for_wife = get_person_details(res["WIFE"])
                for doc in result_for_husband:
                    if doc["birthday"] is not None:
                        hbd = datetime.strptime(doc["birthday"],"%Y-%m-%d %H:%M:%S")
                        husband_age = marriage_date.year - hbd.year
                for doc1 in result_for_wife:
                    if doc1["birthday"] is not None:
                        wbd = datetime.strptime(doc1["birthday"],"%Y-%m-%d %H:%M:%S")
                        wife_age = marriage_date.year - wbd.year
                if wife_age < 14 or husband_age < 14:
                    #wife_marriage_string = "Wife age at the marriage was "+ str(wife_age)
                    #husband_marriage_string = "Husband age at the marriage was "+ str(husband_age)
                    #output('\t' + res["FAMID"] + '\t\t\t%-10s' % res["WIFE"] + " %-10s" % res["HUSBAND"] + '\t\t' + wife_marriage_string + '\t\t' + husband_marriage_string)
                    message = "Wife age at the marriage was "+str(wife_age)+" and Husband age at the marriage was "+str(husband_age)+"."
                    save_invalid_family_for_print(res["FAMID"], "US10", message)