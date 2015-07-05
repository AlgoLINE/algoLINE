class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, heights):
        
        length = len(heights)
        
        if length <= 1 :
            return 0
        
        max = 0
        lIdx = 0
        rIdx = length - 1
        
        while lIdx < rIdx :
            
            # read heights of both sides
            lHeight = heights[lIdx]
            rHeight = heights[rIdx]
            
            # caculate area
            area = min(lHeight, rHeight) * (rIdx - lIdx)
            
            # update max area
            if area > max :
                max = area
            
            # move idx
            if lHeight <= rHeight :
                while lIdx < length and heights[lIdx] <= lHeight :
                    lIdx += 1
            else :
                while rIdx >= 0 and heights[rIdx] <= rHeight :
                    rIdx -= 1
                
        return max