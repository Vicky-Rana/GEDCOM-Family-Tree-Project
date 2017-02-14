"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""


VALID = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE',
             'INDI', 'FAM']

# class for families
class familyClass(object):

    def __init__(self, uid):
        self.uid = uid
        self.marriage = None  
        self.husband = None  
        self.wife = None  
        self.children = []  
        self.divorce = None  

# class for individual persons
class individualPerson(object):

    def __init__(self, uid):
        self.uid = uid  
        self.name = None 
        self.birthday = None 
        self.sex = None 
        self.deathDate = None 
        self.famc = [] 
        self.fams = [] 


# class for every gedcom tag line
class gedcomTagLine(object):

    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        listLine = line.split(' ',)
        # set level of the object
        self.level = int(listLine[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = listLine[1]
            self.arg = listLine[2:]

        if self.level == 0:
            if listLine[1] in VALID:
                self.tag = listLine[1]
                self.arg = None
            else:
                self.tag = listLine[2]
                self.ref = listLine[1]


