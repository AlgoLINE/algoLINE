class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if (size < 3):
            return size
        
        cntOfSameNums = 1
        prevNum = nums[0]
        writeIdx = 1
        
        for idx in xrange (1, size):
            if nums[idx] != prevNum:
                cntOfSameNums = 1
            else:
                cntOfSameNums += 1
                
            if cntOfSameNums <= 2:
                nums[writeIdx] = nums[idx]
                writeIdx += 1
            prevNum = nums[idx]
        
        return writeIdx