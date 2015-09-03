# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        self.result = []
        self.traversal(root)
        
        return self.result
        
    def traversal(self, root):
        if root is None:
            return
        
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)