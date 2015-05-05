class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        elementCount = len(nums)
        
        startIdx = 0
        endIdx = elementCount - 1
        mid = endIdx / 2
        
        while startIdx < endIdx :
            if (mid == startIdx or nums[mid-1] < nums[mid]) and (mid == endIdx or nums[mid] > nums[mid+1]) :
                break
            else :
                if num > startIdx and nums[mid-1] > nums[mid] :
                    endIdx = mid - 1
                elif mid < endIdx and nums[mid] < nums[mid+1] :
                    startIdx = mid + 1
        			
            mid = endIdx + (startIdx - endIdx) / 2
            
        return mid