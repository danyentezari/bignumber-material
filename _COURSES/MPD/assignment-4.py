# Assignment 4
# Write a regular expression that would matches 
# all of the strings in 'cities'.


# ReGex Hint:
# Uppercase letters are indicated '[A-Z]'
# lowercase letters are indicated '[a-z]'
# Space are indicated 's' 

import re
# Your code here...
pattern = ''

# possible matches
cities = [
    'New york',
    'New Mexico',
    'los angeles',
    'NEW ORLEANS',
    'Salt lake city',
    'Oklahoma City'
]

for city in cities:
    match_pattern = re.search(pattern, city)
    
    if match_pattern is not None:
        print(f"Found {match_pattern.group(0)}")