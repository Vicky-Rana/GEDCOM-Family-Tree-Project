from dateutil.relativedelta import relativedelta

from print_data import *
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']

#leap year february
#
#

def US42_rejectIlligitimateDates():
    print ()
