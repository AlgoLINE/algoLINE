# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0: return None
        
        root_node = TreeNode(preorder.pop(0))
        
        root_idx = inorder.index(root_node.val)
        root_node.left = self.buildTree(preorder, inorder[:root_idx])
        root_node.right = self.buildTree(preorder, inorder[root_idx+1:])
        return root_node