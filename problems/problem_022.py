# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    final_list = []
    if is_workday == True:
        if is_sunny == False:
            final_list.append("umbrella")
        final_list.append("laptop")
    else:
        final_list.append("surfboard")
    return final_list

print(gear_for_day(True,False))
