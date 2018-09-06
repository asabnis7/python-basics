def add(a,b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract(a,b):
	print "Subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a,b):
	print "Multiplying %d * %d" % (a, b)
	return a * b
	
def divide(a,b):
	print "Dividing %d / %d" % (a, b)
	return a /b
	
def inverse(a):
	print "Inverting %f" % a
	return 1/a

print "let's do some math"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
inv = inverse(15.0)

print "Age %d, Height %d, Weight %d, IQ %d" % (age, height, weight, iq)
print "Inverse: ", inv

# a puzzle
print "here's a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what

what = age + (height - (weight * (iq/2)))

print what