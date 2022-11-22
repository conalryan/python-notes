#!/usr/bin/env python

"""
Write an interactive script that asks for a president's last name. For each president that matches
print out the presidents date of birth and date of death. If the president is still alive print
3 asterisks.
"""
data = {}

with open('data/presidents.txt') as pres_in:
    for line in pres_in:
        items = line.split(':')
        # Updating dict with pres last name as key
        data.update({items[1]: {'dob': items[3], 'dod': items[4]}})

# print(data)

search_name = input("President's last name? ")

# Exact match
# found = data.get(search_name)
# if found:
#     dod = found.get('dod')
#     if dod == 'NONE':
#         dod = '***'
#     print(f"{found}: {found.get('dob')}, {dod}")

# Case-insensitive search
for k, v in data.items():
    if k.lower().startswith(search_name.lower()):
        dod = v['dod']
        if dod == 'NONE':
            dod = '***'
        print(f"{k}: {v['dob']}, {dod}")