class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        
        length = len(nums)
        k %= length
        
        if k == 0:
            return

        idx = length - 1
        boundIdx = length-k-1
        while idx > boundIdx:                       # position of starting shift
            backup = nums[idx]
            curIdx = idx
            nextIdx = idx - k
            while True:                             # shift until arriving at current position
                nums[curIdx] = nums[nextIdx]
                curIdx = nextIdx
                nextIdx -= k
                if nextIdx < 0:
                    nextIdx += length
                    if nextIdx == idx:              # escape loop
                        break
                    elif nextIdx > boundIdx:        # update boundIdx
                        boundIdx = nextIdx
            nums[curIdx] = backup
            idx -= 1