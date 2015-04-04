# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        nodeQueue = []
        if root is None :
            nodeQueue.append(root)
        
        while len(nodeQueue) is not 0 :
            currentNode = nodeQueue.pop(0)
            
            if currentNode.right is None and currentNode.left is None:
                if currentNode.val == sum :
                    return True;
                    
            if currentNode.right is not None :
                currentNode.right.val += currentNode.val
                nodeQueue.append(currentNode.right)
            if currentNode.left is not None :
                currentNode.left.val += currentNode.val
                nodeQueue.append(currentNode.left)   

        return False
            