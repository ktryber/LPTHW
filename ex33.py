



def learn_while_loop_numbers(a, b):
	i = 0
	numbers = []

	while i < a:
		# this is the value of i before the loop
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + b
		print "numbers now: ",  numbers
		# value of i after before the loop starts over
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num


def for_loop(a, b):

	numbers = []
	for num in range(a, b):
		print numbers
		

		


print for_loop(20, 40)