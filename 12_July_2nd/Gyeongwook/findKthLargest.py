import random

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        start_idx = 0
        end_idx = len(nums)-1
        target_idx = k-1
        
        while True:
            pivot_idx = random.randrange(start_idx, end_idx+1)
            nums[end_idx], nums[pivot_idx] = nums[pivot_idx], nums[end_idx]
            
            large_end_idx = start_idx-1
            
            for idx in range(start_idx, end_idx+1):
                if nums[idx] >= nums[end_idx]:
                    large_end_idx += 1
                    nums[large_end_idx], nums[idx] = nums[idx], nums[large_end_idx]
            
            if large_end_idx == target_idx:
                return nums[target_idx]
            elif large_end_idx < target_idx:
                start_idx = large_end_idx+1
            else:
                end_idx = large_end_idx-1
        
        return nums[k]