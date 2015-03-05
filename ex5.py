name = 'Kris Tryber'
age = 24
height = 69.0 #inches
weight = 155.0 # lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'
inch_centimeter = 2.54 
height_centimeter = height * inch_centimeter
lbs_kilograms = .45
weight_kilograms = lbs_kilograms * weight

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)






