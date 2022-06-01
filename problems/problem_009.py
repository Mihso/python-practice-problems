# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_palindrome(word):
    r_word = reversed(word)
    joined_word = "".join(r_word)
    print(joined_word)

    if word == joined_word:
        return True
    else:
        return False

word_one = "hello"
word_two = "racecar"

word_two.join

result = is_palindrome(word_two)
print(result)

#input:
# word
#output: true or false
#conditions:
#uses built in reversed function and join method
# checks if word is the same forwards and backwards.