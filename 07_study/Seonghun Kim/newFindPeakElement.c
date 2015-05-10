int findPeakElement(int* nums, int numsSize) {
    
    if (numsSize == 0 || numsSize == 1)
        return 0;
    
    int startIdx = 0;
    int endIdx = numsSize-1;
    int midIdx = (endIdx - startIdx + 1)/2;
    
    // idea : jumping to higher parition until arriving at peak.
    while (true) {
        int r = (midIdx+1 == numsSize)? INT_MIN : nums[midIdx+1];   // adjacent right value
        int l = (midIdx-1 == -1)? INT_MIN : nums[midIdx-1];         // adjacent left value
        
        int midVal = nums[midIdx];
        if (midVal > r && midVal > l) {     // if mid value is bigger than both of them,, find peak!
            return midIdx;
        } else if (l > midVal) {            // if left value is bigger than mid value, search left partition 
            endIdx = midIdx-1;
            midIdx = startIdx + (endIdx - startIdx + 1)/2;
        } else {                            // if right value is bigger than mid value, search right partition
            startIdx = midIdx+1;
            midIdx = startIdx + (endIdx - startIdx + 1)/2;
        }
        
    }
}

