# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if len(values) == 0:
        return None
    else:
        maximum = 0
        for i in values:
            if i > maximum:
                maximum = i
        return maximum   
