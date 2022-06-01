# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

#input: list of strings
#output: list of strings added together
# conditions: loop through each item in input
    # create new list by splitting string by "," and converting each into an integer
    #create variable that sums all the integers
    #append variable to the return list

def add_csv_lines(csv_lines):
    final_list = []
    for i in csv_lines:
        temp_list = i.split(",")
        sum = 0
        for n in temp_list:
            sum = sum + int(n)
        final_list.append(sum)
    return final_list

print(add_csv_lines(["1","2,5", "3,4,5"]))

