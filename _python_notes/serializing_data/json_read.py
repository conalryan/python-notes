#!/usr/bin/env python

import json

# Open JSON file for reading
with open('data/solar.json') as solar_in:

    # Load from file object and convert to Python data structure
    solar = json.load(solar_in)

# json.loads(STRING)
# json.load(FILE_OBJECT)
    
# print(solar)

# Solar is just a Python dictionary
print(solar['innerplanets'])
print('*' * 60)
print(solar['innerplanets'][0]['name'])
print('*' * 60)
for planet in solar['innerplanets'] + solar['outerplanets']:
    print(planet['name'])

print("*" * 60)
for group in solar:
    if group.endswith('planets'):
        for planet in solar[group]:
            print(planet['name'])
