#from collections import counter
from print_data import *
def divorcebeforedeath():
	userStoryName('US06')
	results = get_family()
	for res in results:
		if ("HUSBAND" or "WIFE") and "divorce" in res:
			husband = res["HUSBAND"]
			wife = res["WIFE"]
			indi = get_people()
			for temp in indi:
				if husband == temp["ID"] and "deathDate" in temp:
					deathdth = temp["deathDate"]
					divdateh = res["divorce"]
					if divdateh > deathdth:
						message = "Divorced date "+str(divdateh)+", After Husband id "+str(husband)+ " Death on "+str(deathdth)+", therefore Divorce is not valid."
						save_invalid_family_for_print(res["FAMID"], "US06", message)
	
				if wife == temp["ID"] and "deathDate" in temp:
					deathdt = temp["deathDate"]
					divdate = res["divorce"]
					if divdate > deathdt:
						message = "Divorced date "+str(divdate)+", After Wife id "+str(wife)+ " Death on "+str(deathdt)+", therefore Divorce is not valid."
						save_invalid_family_for_print(res["FAMID"], "US06", message)