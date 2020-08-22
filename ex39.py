states = {
    'Oragon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)

print('Michigan has: ', cities[states['Michigan']])

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")

state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

print(cities)
