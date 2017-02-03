# creat a mapping of states to abbreviation
states = {
  'Oregon':'OR',
  'Florida':'FL',
  'California':'CA',
  'New York':'NY',
  'Michigan':'MI'
}

# create a basic set of states and some citie in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonbille'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida has:", states['Florida']

# do it by using the state then cities dict
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreciated %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."
	
# get a city with a default calue
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
