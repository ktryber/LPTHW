print "How old are you?",
age = int(raw_input())

#optional code
if age > 20:
	print "you're old"
else: 
	print "to young"
#optional code

print "How tall are you",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)