# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def max_of_three(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return value1
    elif value2 >= value1 and value2 >= value3:
        return value2
    elif value3 >= value1 and value3 >= value2:
        return value3

print(max_of_three(3,3,1))

#conditions:
#compare value1 and value2
#if value1 < value2
#compare value2 and value3
#if value2 < value3
#compare value1 and value3
#if value1 < value3
#if value1 > value2 and value1 > value3, return value1