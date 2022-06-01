# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

#input: dictionary of keys and values
#output: reversed dictionary
#conditions: find keys and values for each item in input and reverse them

def reverse_dictionary(dictionary):
    new_dict = {}
    for n in dictionary:
        new_dict[dictionary[n]] = n # makes it so that a new key name after the value at n is created in new_dict with a value of n
    return new_dict

print(reverse_dictionary({"key":"values","1":"2"}))