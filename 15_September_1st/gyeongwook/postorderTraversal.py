# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if root is None: return []
        
        result = []
        stack = [root]
        
        while len(stack) > 0:
            current_node = stack.pop()
            
            result.append(current_node.val)
            if current_node.left is not None:
                stack.append(current_node.left)
                
            if current_node.right is not None:
                stack.append(current_node.right)
                
        result.reverse()
        return result