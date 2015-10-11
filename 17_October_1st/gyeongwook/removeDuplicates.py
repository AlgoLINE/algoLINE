class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0
        for each_num in nums:
            if idx == 0 or each_num != nums[idx-1] or idx < 2 or each_num != nums[idx-2]:
                nums[idx] = each_num
                idx += 1
                    
        return idx