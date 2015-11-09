int findMin(int* nums, int numsSize) {
    int minNum = 2147483647;
    int i;

    if (numsSize <= 0)
        return 0;

    if (numsSize == 1)
    {
        return nums[0];
    }

    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] < minNum)
        {
            minNum = nums[i];
        }
    }

    return minNum;
}