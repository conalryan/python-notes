#!/usr/bin/env python

import json

# Python data structure
george = [
    {
        'num':1,
        'lname':'Washington',
        'fname':'George',
        'dstart':[1789,4,30],
        'dend':[1797,3,4],
        'birthplace':'Westmoreland County',
        'birthstate':'Virginia',
        'dbirth':[1732,2,22],
        'ddeath':[1799,12,14],
        'assassinated': False,
        'party':'no party',
    },
    {
        'foo':'bar'
    }
]

# Dump structure to JSON string
js = json.dumps(george, indent=8)
print(js)

# Open file for writing
with open('george.json', 'w') as JS:

    # Dump structure to JSON file using open file object
    json.dump(george, JS)
