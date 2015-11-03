class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0, 0]
        for idx in xrange(0, len(nums)):
            temp[idx & 1] += nums[idx]
            if (temp[(idx-1) & 1] >= temp[idx & 1]):
                temp[idx & 1] = temp[(idx-1) & 1]
        return max(temp[0], temp[1])