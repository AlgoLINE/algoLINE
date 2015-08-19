class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        result = [[]]
        nums.sort()
        
        for each in nums:
            count = len(result)
            for idx in range(count):
                elem = result[idx][:]
                elem.append(each)
                if elem not in result:
                    result.append(elem)
        
        return result