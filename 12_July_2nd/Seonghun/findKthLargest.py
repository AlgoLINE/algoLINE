# import random

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        
        lIdx = 0
        rIdx = len(nums)-1
        
        while True:
            idx = self.partition(nums, lIdx, rIdx)
        
            if idx + 1 < k:
                lIdx = idx+1
            elif idx + 1 > k:
                rIdx = idx-1
            else:
                return nums[idx]
        
    def partition(self, nums, lIdx, rIdx):
        
        pivotIdx = rIdx 
        # pivotIdx = self.getPivotIdx(lIdx, rIdx)
        pivot = nums[pivotIdx]
        # self.swap(nums, pivotIdx, rIdx)
        
        divIdx = lIdx
        for idx in range(lIdx, rIdx):
            if nums[idx] > pivot:
                self.swap(nums, divIdx, idx)
                divIdx += 1
            
        self.swap(nums, divIdx, rIdx)
        
        return divIdx
        
    # def getPivotIdx(self, lIdx, rIdx):
    #     return random.randrange(lIdx, rIdx+1)
        
    def swap(self, nums, aIdx, bIdx):
        temp = nums[aIdx]
        nums[aIdx] = nums[bIdx]
        nums[bIdx] = temp
        