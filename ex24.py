print "Let's practice"

print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------"
print poem
print "-------------"

five = 10 - 2 + 3 - 6
print "This is %d" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans/1000
	crates = jars/100
	return jelly_beans, jars, crates
	
start = 10000
beans, jars, crates = secret_formula(start)

print "With a start of %d" % start
print "We have %d beans, %d jars, %d crates" % (beans, jars, crates)

start = start/10
print "Also do it like this"
print "We have %d beans, %d jars, %d crates" % secret_formula(start)