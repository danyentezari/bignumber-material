class LinkedListNode:
    def __init__(self, value_to_insert, next_node=None):
        self.data = value_to_insert
        self.next = next_node
        


class LinkedList:
    def __init__(self, start_param):
        self.start = LinkedListNode(start_param)
        self.last = self.start
    
    def append_node(self, value_to_insert):
        # Create a new node
        new_node = LinkedListNode(value_to_insert)
        
        # Point 'next' of the current last to the new node
        self.last.next = new_node
        
        # Make the new node the last node
        self.last = new_node
    
        
    
    def pop_node(self, node_to_remove=False):
            
        # Create a node to keep track of the node that is n-1
        n_1_node = None
        
        # Start searching at the beginning of the linked ist
        next_node = self.start
        
        # Keep traversing the linked list until the last node is reached
        # This is done to find the node at index n-1
        while(next_node.next is not None):     
            # Keep updating n_1_node
            n_1_node = next_node
            
            # Point next_node to the node that comes next 
            next_node = next_node.next
        

        # Delete the last node
        del self.last
        
        # Update the node at n-1 to reflect the change
        n_1_node.next = None
        
        # Setting the last node to the node at n-1
        self.last = n_1_node
            
            
          

        


# Create the linked list with a root node
linked_list = LinkedList("A") 
print(linked_list.last.data)

linked_list.append_node("B")
linked_list.append_node("C")

linked_list.pop_node()
linked_list.pop_node()

print(linked_list.last.data)
