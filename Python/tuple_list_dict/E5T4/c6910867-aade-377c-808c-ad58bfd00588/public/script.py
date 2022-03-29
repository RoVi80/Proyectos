#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):

    if wa_nrs==[]:
        return []
    else:
        j_possible_nrs = []
        every_possible_j = []
        #for number in n:
        #print(number)
        for item in range(2, 10):
            for x in range(10):
                #print(x)
                every_possible_j.append(n[:item] + str(x) + n[item:])
        #print(every_possible_j)
        for nrs in every_possible_j:
            if nrs in wa_nrs:
                j_possible_nrs.append(nrs)
        return j_possible_nrs
    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))