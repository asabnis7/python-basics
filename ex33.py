numbers = []

def looper(limit, incre):
	i = 0
	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += incre
		print "Numbers now: ", numbers
	
		print "At the bottom i is %d" % i
	

print "What limit?"	
limit = int(raw_input("> "))
print "What increment?"
increment = int(raw_input("> "))

looper(limit, increment)
	
print "The numbers: "

for num in numbers:
	print num