class DoublyLinkedListNode:
    def __init__(self, value_to_insert, next_node=None, prev_node=None):
        self.data = value_to_insert
        self.next = next_node
        self.prev = prev_node
        


class DoublyLinkedList:
    def __init__(self, start_param):
        self.start = DoublyLinkedListNode(start_param)
        self.last = self.start
    
    def append_node(self, value_to_insert):
        # Create a new node
        new_node = DoublyLinkedListNode(value_to_insert, next_node=None, prev_node=self.last)
        
        # Point 'next' of the current last to the new node
        self.last.next = new_node
        
        # Make the new node the last node
        self.last = new_node
        
    def pop_node(self):
       prev = self.last.prev 
       del self.last
       self.last = prev 
       

    def count(self):
        # Complete the code to count the total number of elements
        # in the tree
        # Your code here
        
        counter = 0
        next_node = self.start
        while(next_node is not None):
            counter += 1
            next_node = next_node.next
                
        return counter
        



d_linked_list = DoublyLinkedList("A") 

d_linked_list.append_node("B")
d_linked_list.append_node("C")
d_linked_list.append_node("D")

# Test the .count() method
print(d_linked_list.count())


# print(d_linked_list.last.data)
# d_linked_list.pop_node()
# d_linked_list.pop_node()
