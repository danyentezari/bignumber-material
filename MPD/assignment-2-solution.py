# Python Assignment 2:
# See steps 1 to 4 in this file.
# DO NOT CHANGE ANY OF THE GIVEN LINES OF CODE. 
data = [
    {
        "id": "0002",
        "company": "Netflakes",
        "revenue": 1000000
    },
    {
        "id": "0001",
        "company": "Microsoap",
        "revenue": 2000000
    },
    {
        "id": "0003",
        "company": "Burger Bing",
        "revenue": 3000000,
    }
]






# 1 - Swap the "id" of the first and second elements.
#     Note: do this without hardcoding the values.
#     Hint: you can try using a temporary variable. 
#
#     Your result should produce:
#     {
#         "id": "0001",
#         "company": "Netflakes",
#         ...
#     },
#     {
#         "id": "0002",
#         "name": "Microsoap",
#         ...
#     },
#    ...




# 2 - Complete the algorithm that will recursively 
#     aggregate the values for every "revenue"
#     in "data".  
#     Note: do not use either for or while loop.
#     Hint: you can try adding another parameter
#     to the function.    
#
#     The function should return 6000000
def recursive_sum(data):
    
    # Your code...
    
    return #???



def recursive_sum2(data, total=0, index=0):
    
    total += data[index]['revenue']
    
    if index < len(data) - 1:
        total = recursive_sum2(data, total, index + 1)
    
    return total

print(recursive_sum2(data))