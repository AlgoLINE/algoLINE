class Solution(object):
    def findMin(self, nums):
        for idx in range(1, len(nums)):
            if nums[idx-1] > nums[idx]:
                return nums[idx]
        
        return nums[0]
        