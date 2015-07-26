class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        
        length = len(nums)
        k %= length
        
        if k == 0:
            return
        
        # backup
        backup = nums[(length-k):length]
        
        # k-shift
        for idx in range(length-1, k-1, -1):
            nums[idx] = nums[idx-k]
        
        # restore backuped values
        for idx in range(0, len(backup)):
            nums[idx] = backup[idx]