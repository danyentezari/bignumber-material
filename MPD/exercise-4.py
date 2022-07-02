# Python Exercise 4
# Do steps (1) and (2)
n1 = {
    "data": 'A',
    "next": None
}

n2 = {
    "data": 'B',
    "next": None
}

n3 = {
    "data": 'C',
    "next": None
}

n4 = {
    "data": 'D',
    "next": None
}

n1['next'] = n2
n2['next'] = n3
n3['next'] = n4
linked_list = n1
last_element = n4

# Reference
# def list_search(list_param, search):
#     print(f"Searching {list_param['data']} for {search}")
    
#     if list_param['data'] == search:
#         return list_param
#     else:
#         return list_search(list_param['next'], search)
        

# print(list_search(linked_list, "D"))



# (1) Complete the function for appending nodes
# to the linked list
# def append_node(linked_list_param, value_to_insert):
#     # {
#     #     "data": '',
#     #     "next": None
#     # }
#     # ...
    
#     # If 'next' is None (i.e, this is the last element in the linked list)
#     if linked_list_param['next'] == None:
#         # Append the new element
#         linked_list_param['next'] = {
#             'data': value_to_insert,
#             'next': None
#         }
#     # Otherwise, traverse the linked list until last element reached
#     else:
#         return append_node(linked_list_param['next'], 'E')



def append_node(value_to_insert, last_element_param):
     
    # Create a new element
    new_element = {
         'data': value_to_insert,
         'next': None
    }
    
    # Append the new element to the last_element
    last_element_param['next'] = new_element
    
    # Point the last_element to the new_element
    last_element_param = new_element
    return last_element_param
   


 
  

# (2) Append the letters 'E' to 'H' to the 'linked_list'
last_element = append_node('E', last_element)
last_element = append_node('F', last_element)
last_element = append_node('G', last_element)
print(linked_list)  