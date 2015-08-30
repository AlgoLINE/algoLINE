# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        iIdx = pIdx = 0
        size = len(preorder)
        valToNode = {}
        root = None
        
        while pIdx < size:
            # find parent
            parent = None
            if iIdx > 0 and iIdx < size:
                while iIdx < size and valToNode.has_key(inorder[iIdx]):
                    iIdx += 1
                parent = valToNode[inorder[iIdx-1]]
            
            # make left skewed tree
            preNode = subRoot = None
            while pIdx < size:
                val = preorder[pIdx]
                pIdx += 1
                valToNode[val] = node = TreeNode(val)
                if subRoot == None:
                    subRoot = node
                else:
                    prenode.left = node
                
                if val == inorder[iIdx]:
                    iIdx += 1
                    break
                prenode = node
            
            # link it to parent's right
            if parent == None:
                root = subRoot
            else:
                parent.right = subRoot
    
        return root