import re

pattern = 'a(p|l)p{0,}(l|e){0,}(e|l){0,}'

user_input = input("Enter brand name: ")

match_apple = re.search(pattern, user_input)

if match_apple is not None:
    print(match_apple.group(0))
    print("Did you mean apple?")