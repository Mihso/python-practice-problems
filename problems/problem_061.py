# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
#     * input:   [1, 1, 1, 1]
#       returns: [1]
#     * input:   [1, 2, 2, 1]
#       returns: [1, 2]
#     * input:   [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]
def remove_duplicates(numbers):
    final_list = []
    intermediate = {}
    for i in numbers:
        intermediate[i] = "0"
    for n in intermediate:
        final_list.append(n)
    return final_list

print(remove_duplicates([1,2,2,2,3,4,4,5,6,7]))
