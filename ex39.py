# create mapping of states to abbreviations

states = {
	'Oregon':'OR',
	'California':'CA',
	'Florida':'FL',
	'New York':'NY',
	'Michigan':'MI',
	'Georgia':'GA'
}
# create basic set of states and some cities in them

cities = {
	'CA': 'San Francisco',
	'NY': 'New York',
	'GA': 'Atlanta'
}

# add some more cities
cities['MI'] = 'Detriot'
cities['OR'] = 'Portland'
cities['FL'] = 'Jacksonville'

print '-'*10
print "NY state has: ", cities['NY']
print "GA state has: ", cities['GA']

print '-'*10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-'*10
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)

print '-'*10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
print '-'*10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-'*10
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas"

city = cities.get('TX', 'Does not Exist')
print "The city for the state of 'TX' is: %s" % city

print '-'*10
print "Let's see some more states"

india = {
	'MH': 'Maharashtra',
	'TN': 'Tamil Nadu',
	'PN': 'Punjab',
	'DL': 'Delhi',
	'GJ': 'Gujarat'
}

for abbrev, state in india.items():
	print '%s is %s' % (abbrev, state)
	
print '-'*10
del india['PN']
india['KR'] = 'Karnataka'
print "KR is %s" % india['KR']