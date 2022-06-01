# Complete the sum_of_first_n_numbers function which accepts
# a numerical limit and returns the sum of the numbers from
# 0 up to and including limit.
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+1=1
#   * 2 returns 0+1+2=3
#   * 5 returns 0+1+2+3+4+5=15
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#input: a number

#output: None if input is less than 0, 0 if input is 0, sum of numbers from 0 to the input

def sum_of_first_n_numbers(limit):
    # if the limit is less than zero, return None
    # have a empty variable that will be returned
    # for loop that has a range from 0 to the limit given
    if limit < 0 :
        return None
    else:
        total = 0
        for i in range(0,limit+1):
            total = total + i
        return total

print(sum_of_first_n_numbers(5))