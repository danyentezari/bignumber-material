# Python Exercise 3
# Write a recursive function, 'recursive_uppercase', that
# will take a list of letter as argument and
# recursively make the letters uppercase.
letters = ['a','b','c','d','e']

# your function should convert the values
# inside 'letters' to ['A','B','C','D','E']
#
# Hint: the string method to make a character uppercase
# is .upper()
#
#


# Solution 1 (Modify the original global list)
# def recursive_uppercase(list_param, index=0):
#     if index < len(list_param):
#        list_param[index] = list_param[index].upper()
#        recursive_uppercase(list_param, index+1)

# recursive_uppercase(letters)


# Solution 2 (Create a new list)
def recursive_uppercase(list_param, index=0, new_list_param=[]):
    if index < len(list_param):
        # Make the letter of original list uppercase
        letter_uppercase = list_param[index].upper()
        # Put it inside the new list
        new_list_param.append( letter_uppercase  )
        # Call the function again with the new list
        recursive_uppercase(list_param, index+1)
        # Recursion
            # Recursion
                #....
                    # Recursion
        
        return new_list_param


letters = recursive_uppercase(letters)


# Test the final result with this print()
# print(letters)
# This should appear in the terminal:
# ['A','B','C','D','E']
