"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""
import argparse
import os
from prettytable import PrettyTable
from src.gedParser import GEDCOMParser


#Default File Path

FILENAME = 'gedcom_files/myFTree.ged'

p1 = PrettyTable()
p2 = PrettyTable()

#This is the function to print the family and individual details in a pretty table
def printPretty(individual, families):
    print('\n\t\t\t-----------------------------------------------------')
    print('\n\t\t\t\t\tINDIVIDUAL DETAILS ')
    print('\n\t\t\t-----------------------------------------------------')
    p1.field_names = ["UID","NAME","BIRTHDATE","SEX","DAETH DATE","FAMC","FAMS"]
    for line in individual:
        attribute = vars(line)
        p1.add_row(attribute.values())

    print(p1)
    
    print('\n\t\t\t-----------------------------------------------------')
    print('\n\t\t\t\t\tFAMILY DETAILS ')
    print('\n\t\t\t-----------------------------------------------------')

    p2.field_names = ["FID","MARRIAGE","HUSBAND","WIFE","CHILDREN","DIVORCE"]
    for line in families:
        attribute = vars(line)
        p2.add_row(attribute.values())
#        print (', '.join("%s: %s" % item for item in attribute.items()))
    print(p2)


# Main Funciton 
def main():
    
    parser = argparse.ArgumentParser() # Allow for args to be passed for filename
    action = parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME,
                        help="Specify file name" + FILENAME)

    args = parser.parse_args()
    path = args.file
    if os.path.exists(path):
        print("PATH VERIFIED...")
        individual, families = GEDCOMParser(path)
    else:
        print("[!!] FILE \"%s\" DOESN'T EXISIT.\n Terminiating..." % path)
        exit(-1)
    #printing values
    printPretty(individual, families)

if __name__ == '__main__':
    main()