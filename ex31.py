print "You enter a dark room with two doors. Which door do you take?"

door = raw_input("> ")

if door == '1':
	print "There's a giant bear here eating cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	
	if bear == '1':
		print "The bear eats your face off. Great job!"
	elif bear == '2':
		print "The bear eats your legs off. Good one!"
	else:
		print "Well, doing %s was more useful. The bear runs away." % bear

elif door == '2':
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding yelling revolvers"
	
	insane = raw_input("> ")
	
	if insane == '1' or insane == '2':
		print "Your body survives, but your mind melts to jello. Good job!"
	else:
		print "The insanity rots your eyes into muck. Great one!"
	
else: print "You stumble around and fall on a knife and die. R.I.P." 	