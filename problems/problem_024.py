# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if len(values) == 0:
        return None
    else:
        total = 0
        for n in values:
            total = total + n
        return (total/len(values))

print(calculate_average([]))
