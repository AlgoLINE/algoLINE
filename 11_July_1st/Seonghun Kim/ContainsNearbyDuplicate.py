class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        
        length = len(nums)
        dict = {}                # hash map
        
        for idx in range(0, length):
            value = nums[idx]
            if dict.has_key(value):             # if there was same 'value' before
                latestIdx = dict[value]
                if idx - latestIdx <= k:            # just check latest idx of the 'value'
                    return True
            dict[value] = idx
                
        return False