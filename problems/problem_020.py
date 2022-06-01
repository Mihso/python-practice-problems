# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    if len(attendees_list) >= (len(members_list)/2):
        return True
    else:
        return False

print(has_quorum([1,2,3,4,5],[2,4,5,6,7,8,3,4,5,6,7,8,9,0,5,4,3]))