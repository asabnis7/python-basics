name = 'Arjun Sabnis'
age = 21
height = 72
weight = 160
weight_kg = 2.2*weight
height_cm = 2.54*height
eyes = 'brown'
teeth = 'white'
hair = 'Black'

print "Let's talk about %s." % name
print "He's about %d inches tall" % height
print "He's %d pounds heavy" % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "This shit is weird, %r %r %r" % (age, age, age)

print "In real units, height is %r and weight is %r. %r boy" % (height_cm, weight_kg, eyes)