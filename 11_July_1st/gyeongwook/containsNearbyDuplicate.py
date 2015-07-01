class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        lookup_table = {}
        for i in range(len(nums)):
            if nums[i] in lookup_table and i - lookup_table[nums[i]] <= k:
                return True
                        
            lookup_table[nums[i]] = i
                    
        return False