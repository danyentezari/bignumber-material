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


def list_search(list_param, search):
    
    if list_param['data'] == search:
        return list_param
    else:
        return list_search(list_param['next'], search)
        

print(list_search(linked_list, "D"))