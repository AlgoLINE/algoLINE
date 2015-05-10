bool canJump(int* nums, int numsSize) {
    int targetIdx = numsSize-1;
    int canReach[numsSize];     // Store whether each item can reach to next target item or not
    
    for(int i = numsSize-2 ; i >= 0 ; i--) {
        if (targetIdx - i <= nums[i]) {        // if current idx can reach to target idx
            canReach[i] = true;
            targetIdx = i;
        }
        else {
            canReach[i] = false;
        }
    }
    
    return canReach[0];
    
}