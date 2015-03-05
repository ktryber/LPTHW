
# this variable holds a string and with a formatter. 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#the formatter here inputs the variables from left to right into the string.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarous = False
# the %r is used to print out the raw data of a variable it's not used for users more for debugging.
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarous

w = "This is the left side of..."
e = "a string with a right side"

# the + symbol represents concatenation which combines these two variables and the strings inside of them.
print w + e