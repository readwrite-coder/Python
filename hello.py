print("hello world")

age_1 = 5 #cannot start variable with a number.
#by convention, we do not capitalize variables. 

result = 10 / 3 #automatically does float division
print(result)

import math
print(math.floor(result)) # always executed inner parentheses first, then outer.
print(math.ceil(result)) # rounds up to largest integer, floor rounds down

result_new = 10 // 3 #integer division provided with '//' operator
print(result_new)

#MODULUS
number = 345349
limit = 100
print("modulus: " + str(number % limit)) #result will be less than 10; if limit is 100, result less than 100

pwer = math.ceil(math.pow(10,2))
print(pwer)
#'literal' : anytime we type out a value, in contrast to a variable; literal is value itself.
# comments are no prefaced by 2 //forward dashes, but instead with a pound signal (hashtag)

"""
print("trying to execute statement)
if we want block comments, use three double quotes.
"""
