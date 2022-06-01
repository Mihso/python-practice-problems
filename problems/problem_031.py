# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#input: list of values
#output: None if no values in list, sum of each item squared

#conditions:
# if no values in list, return None
# go through each value in list
# add each value squared to a variable
# return variable

def sum_of_squares(values):
    if len(values) == 0:
        return None
    else:
        total = 0
        for n in values:
            total = total + (n*n)
        return total 

print(sum_of_squares([1,0,-1]))