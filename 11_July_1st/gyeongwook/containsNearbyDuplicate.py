class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        lookup_table = {}
        for i in range(len(nums)):
            if nums[i] in lookup_table:
                for each in lookup_table[nums[i]]:
                    if i - each <= k:
                        return True
                        
                lookup_table[nums[i]].append(i)
            else:
                lookup_table[nums[i]] = [i]
                    
        return False