# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# input:
# age
# has_consent_form

# output:
# true or false

#conditions:
#compare age to the number 18, check if has_consent_form is true
# if age > 18 and if has_consent_true is true
# return true

from operator import truediv


def can_skydive(age, has_consent_form):
    if age > 18 or has_consent_form:
        return True
    else:
        return False

age_one = 25
has_consent_form_one = True

age_two = 17
has_consent_form_two = False

result_one = can_skydive(age_one, has_consent_form_one)

print(result_one)
