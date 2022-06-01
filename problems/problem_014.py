# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#input: ingredients list

#output: true or false

# conditions:
#function can make pasta with ingredients
    # check each of ingredients you do have
        # check if have flour
        # check if have eggs
        # check if have oil
    # anyone of those ingredients are missing, can't make pasta

def can_make_pasta(ingredients):
    check_flour = False
    check_eggs = False
    check_oil = False
    for i in ingredients:
        if i == "flour":
            check_flour = True
        elif i == "eggs":
            check_eggs = True
        elif i == "oil":
            check_oil = True
    if check_flour == True and check_eggs == True and check_oil == True:
        return True
    else:
        return False
print(can_make_pasta(["eggs", "oil", "flour"]))
