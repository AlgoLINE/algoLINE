# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def inorderTraversal(self, root):
        
        lInorder = []
        
        def inorder(root):
            if (root != None):
                inorder(root.left)
                lInorder.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return lInorder