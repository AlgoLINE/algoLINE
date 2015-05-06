class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        lastIdx = len(nums) - 1
        
        mostFarIdx = 0
        
        for idx in range(lastIdx + 1) :
            if idx > mostFarIdx :
                return False
                
            mostFarIdx = max(mostFarIdx, nums[idx] + idx)
            
            if mostFarIdx >= lastIdx :
                break;
        
        return True