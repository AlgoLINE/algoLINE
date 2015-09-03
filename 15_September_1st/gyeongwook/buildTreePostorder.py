# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0: return None
        
        root_node = TreeNode(postorder.pop())
        
        root_idx = inorder.index(root_node.val)
        root_node.right = self.buildTree(inorder[root_idx+1:], postorder)
        root_node.left = self.buildTree(inorder[:root_idx], postorder)
        return root_node