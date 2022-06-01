# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def minimum_value(value1, value2):
    if value1 < value2:
        # if value1 is lower than value2
        return value1 
        # return value 1 if it's smaller
    elif value1 > value2:
        #if value 1 is higher than value 2
        return value2
        # return value2 if it's smaller
    else:
        return value1
        #else return value1, since it doesn't matter which one is returned since they are the same

# Questions:
#input:
#2 values

#output:
#the minimum of the two values

#conditions:
#if value1 < value2:
#