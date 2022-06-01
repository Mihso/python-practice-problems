# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):
    if len(s) == 0:
        return s
    else:
        comp = ""
        comp_list={} # create list of unqiue letters that have been found
        for n in s:
            comp_list[n] = 1 # the value of the key at comp_list[n] doesn't matter as much as the fact that the comp_list[n] key exists at all.
        for n in comp_list:
            comp = comp + n # add the key at n to comp
        return comp

print(remove_duplicate_letters("abbxxxssss"))
