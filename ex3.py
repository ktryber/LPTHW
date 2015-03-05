# + plus == addition
# - minus == subtraction
# / slash == division
# * asterik == multiplication
# % percent == Mostly that's just how the designers chose to use that symbol. In normal writing you are correct to read it as a "percent." In programming this calculation is typically done with simple division and the / operator. The % modulus is a different operation that just happens to use the % symbol.
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal
# == equal-to

# Python always uses the orders of operations PEMDAS
# Parenthesis
# Exponents
# Multipication
# Division
# Addition
# Subtraction

print "I will now count my chickens:"

# divides 30 by 6 then adds 25
print "Hens", 25 + 30 / 6

# 
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's false."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "This is rate per mile for 1004 miles at $2/mile", 1003.0 * 2.3