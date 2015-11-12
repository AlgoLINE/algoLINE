class Solution(object):
    def rob(self, nums):
        if nums is None: return 0
        
        length = len(nums)
        if length == 0: return 0
        
        self.lookup_table = {}
        return self.recursion(nums)
        
    def recursion(self, nums):
        if nums is None: return 0
        
        length = len(nums)
        if length == 0: return 0
        
        if length in self.lookup_table:
            return self.lookup_table[length]
        else:
            ret = max(self.recursion(nums[1:], self.recursion(nums[2:]) + nums[0]))
            self.lookup_table[length] = ret
            return ret