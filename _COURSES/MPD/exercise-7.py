# Exercise 7
# Write a regular expression for finding possible matches 
# for the word 'tesla

import re

# Your code here...
pattern = 'te(s){1,}(l|(a){0,}){1,}'

# possible matches
possible_matches = [
    'tesla',
    'tesssla',
    'tesl',
    'tesal'
]

for possible_match in possible_matches:
    match_tesla = re.search(pattern, possible_match)
    
    if match_tesla is not None:
        print(f"Found tesla in {match_tesla.group(0)}")