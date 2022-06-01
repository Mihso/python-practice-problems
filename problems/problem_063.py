# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(word):
    new_word = ""
    for n in word:
        if n == "z" or n == "Z":
            letter = ord(n)
            letter = letter - 25
            letter = chr(letter)
        else:
            letter = ord(n)
            letter = letter + 1
            letter = chr(letter)
        new_word = new_word + letter
    return new_word

print(shift_letters("Zello"))
