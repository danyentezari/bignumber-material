class RBNode:
    def __init__(self, key_arg, color_arg="BLACK", p_arg=None, left_arg=None, right_arg=None):
        self.key = key_arg
        self.color = color_arg
        self.p = p_arg
        self.left = left_arg
        self.right = right_arg
        

class RBTree:
    def __init__(self):
        # Create a node (by default the color will be black)
        self.nil = RBNode(0)
        
        # Set the root of the tree to nil
        self.root = self.nil
    
    
    def rb_insert(self, new_node):
        
        # Temporarily point the tree 'nil'
        nil = self.nil
        
        # Keep track of the root
        root = self.root
        
        
        while root != self.nil:
            nil = root
            if new_node.key < root.key:
                root = root.left
            else:
                root = root.right
                
        new_node.parent = nil
        
        # If first element being created, make the 
        # variable 'nil' the nil of treee
        if nil == self.nil:
            self.root = new_node
         
        # if the key of new node is less than
        # the 'nil', assign it to the left    
        elif new_node.key < nil.key:
            nil.left = new_node
          
        # if the key of new node is greater than
        # the 'nil', assign it to the right   
        else:
            nil.right = new_node
        
        # give the new node a left leaf
        new_node.left = self.nil
        
        # give the new node a right leaf
        new_node.right = self.nil
        
        # set the color of the new node to red
        new_node.color = "RED"
        
        # self.rb_insert_fixup(new_node)
        

rbtree = RBTree()

rbtree.rb_insert(RBNode(3))
rbtree.rb_insert(RBNode(4))

print(rbtree.root.right.key)