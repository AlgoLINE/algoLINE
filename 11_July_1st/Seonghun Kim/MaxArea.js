/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(heights) {
    
    var length = heights.length;
    
    if (length <= 1)
        return 0;
        
    var max = 0;
    var lIdx = 0;
    var rIdx = length -1;
        
    while (lIdx < rIdx) {
        
        // read heights of both side
        lHeight = heights[lIdx]
        rHeight = heights[rIdx]
            
        // caculate area
        var area = Math.min(lHeight, rHeight) * (rIdx - lIdx);
            
        // update max area
        if (area > max)
            max = area;
            
        // move idx
        if (lHeight <= rHeight) {
            while (lIdx < length && heights[lIdx] <= lHeight) 
                lIdx += 1;
        } else {
            while (rIdx >= 0 && heights[rIdx] <= rHeight)
                rIdx -= 1;
        }
    }
            
    return max;
};