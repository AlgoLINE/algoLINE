class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        length = len(nums)
        lookup_table = {}
        
        for index2 in range(length) :
            if target-nums[index2] in lookup_table :
                return [lookup_table[target-nums[index2]]+1, index2+1]
            else :
                lookup_table[nums[index2]] = index2