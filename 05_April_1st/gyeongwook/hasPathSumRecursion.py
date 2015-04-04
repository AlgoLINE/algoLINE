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
        if root is None :
            return False

        return self.recursion(root, 0, sum)

    def recursion(self, node, prevSum, sum):
        if node is None :
            return False

        currentSum = prevSum + node.val

        if node.left is None and node.right is None :
            if currentSum == sum :
                return True
            else :
                return False

        return self.recursion(node.left, currentSum, sum) or self.recursion(node.right, currentSum, sum)