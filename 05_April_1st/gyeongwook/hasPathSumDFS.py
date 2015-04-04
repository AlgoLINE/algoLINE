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
        nodeTrace = []
        currentNode = root
    
        while currentNode is not None :
            if currentNode.left is not None :
                if currentNode.right is not None :
                    currentNode.right.val += currentNode.val
                    nodeTrace.append(currentNode.right)
                
                currentNode.left.val += currentNode.val
                currentNode = currentNode.left
                continue
            elif currentNode.right is not None :
                currentNode.right.val += currentNode.val
                currentNode = currentNode.right
            else :
                if currentNode.val == sum :
                    return True
    
                if len(nodeTrace) is not 0 :
                    currentNode = nodeTrace.pop()
                else :
                    currentNode = None
        
        return False