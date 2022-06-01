# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

#function halve the list with single list as input
    #create first new list
    #create second new list
    # boolean if length of list is odd
    #check if there are an odd number of items in list
        # if there are, subtract one from length
            # set boolean to true
        # otherwise note
        # split length of list in half
    #for item in range of first item to half.
        # add items from original list to first new list
    #for item in range of half to item.
        # add rest of items from original lists
    # return both lists

def halve_the_list(single_list):
    first_list = []
    original_length = len(single_list)
    second_list = []
    odd = False
    if len(single_list)%2 == 0:
        odd = False
    else:
        original_length = original_length - 1
        odd = True
    split_point = int(original_length / 2)
    if odd:
        split_point = split_point + 1

    for i in range(0,split_point):
        first_list.append(single_list[i])
    for i in range(split_point, len(single_list)):
        second_list.append(single_list[i])
    return first_list, second_list

print(halve_the_list([1,2,3,4,5]))