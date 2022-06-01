# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#conditions:
# return None if the length of values is less than 2

# input: list of values
# output: second largest value in give list
#conditions:
# if value found that is larger than current largest, keep track of previous largest value
# go throught list to find values,
# check in case there are second largest values even if the largest value was already found
def find_second_largest(values):
    if len(values) < 2:
        return None
    else:
        largest = 0
        second_largest = 0
        for n in values:
            if n > largest or n > second_largest:
                if n > largest:
                    second_largest = largest
                    largest = n
                else:
                    second_largest = n
        return second_largest

print(find_second_largest([1,2,5,4,7,6]))