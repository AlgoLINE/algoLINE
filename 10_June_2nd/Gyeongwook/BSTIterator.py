# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.current_node = TreeNode(None)
        self.current_node.right = self.most_small_node(root)
    
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        print self.current_node.val
        
        if self.current_node is None:
            return False
            
        return self.current_node.right is not None or len(self.stack) > 0
    
    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            if self.current_node.right is None:
                    self.current_node = self.stack.pop()
            else:
                self.current_node = self.most_small_node(self.current_node.right)
                
            return self.current_node.val
    		
    	return None
    	
    def most_small_node(self, root):
        current_node = root
        
        if current_node is not None:
            while current_node.left is not None:
                self.stack.append(current_node)
                current_node = current_node.left
        		
        return current_node

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())