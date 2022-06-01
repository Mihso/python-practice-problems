# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"

def pad_left(number, length, pad):
    final_string = str(number) # converts integer to string
    stin_length = len(final_string) # gets length of converted integer
    for i in range(0,length - stin_length): #loops based on given length.
        final_string = pad + final_string # adds pad to the final string
    return final_string

print(pad_left(11,5,"*"))