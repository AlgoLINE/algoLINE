class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums is None or len(nums) == 0:
            return None;
        
        return self.add_node(0, len(nums)-1, nums)
        
    def add_node(self, start, end, nums):
        idx = (start+end) / 2
        new_node = TreeNode(nums[idx])
        if start < idx:
            new_node.left = self.add_node(start, idx-1, nums)
        if idx < end:
            new_node.right = self.add_node(idx+1, end, nums)
            
        return new_node
        