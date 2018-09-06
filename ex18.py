def print_three(*args):
	arg1, arg2, arg3 = args
	print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)
	
def print_two(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
def print_none():
	print "I got nothing"
	
print_three('A', 'R', 'S')
print_two('A','S')
print_one('RIP')
print_none()