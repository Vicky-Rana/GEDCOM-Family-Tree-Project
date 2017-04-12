from datetime import datetime, timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
#from collections import counter
import re
import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
from all_db_operations import *
from print_data import *

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

def fewer_than15_siblings():
    userStoryName('US15')
    """ US15 -- Each Family should have less than 15 Siblings """   
    families = get_family()
    for family in families:    
        if 'CHILDREN' in family:
            if len(family['CHILDREN']) >= 15:
                message = "Siblings in this family is greater than or equal to 15"
                save_invalid_family_for_print(family["FAMID"], "US15", message)
            
            
 
