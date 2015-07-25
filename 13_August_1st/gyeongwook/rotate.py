class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotaterotate(self, nums, k):
        length = len(nums)
        if length == 0:
            return
        
        k = k%length
        if k == 0:
            return
        
        modified = length
        
        for start in range(length):
            if start == modified:
                break
            
            destination = (start+k)%length
            current_idx = start-1
            value_to_move = nums[start]
            
            while current_idx != start:
                modified = destination if destination < modified and destination != start else modified
                
                value_to_move, nums[destination] = nums[destination], value_to_move
                current_idx = destination
                destination = (destination+k)%length