int findPeakElement(int* nums, int numsSize) {
        int dir = 1;
        for (int i = 1 ; i < numsSize ; i++) {
            int newDir = nums[i] - nums[i-1];
            if (newDir * dir < 0)
                return i-1;
            dir = newDir;
        }
        
        if (dir * -1 < 0)
            return numsSize-1;    
            
        return 0;    
}