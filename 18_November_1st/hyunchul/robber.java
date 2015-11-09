public class Solution {
    public int rob(int[] nums) {
        if (nums.length <= 0)
        {
            return 0;
        }
        
        int numsSize = nums.length;
        
        if (numsSize == 1)
        {
            return nums[0];
        }
        
        int ary[] = new int [numsSize];
        
        for (int i = 0; i < numsSize; i++)
        {
            if (i == 0 || i == 1)
            {
                ary[i] = nums[i];
            }
            
            if (i + 2 < numsSize)
            {
                int tmpSum = ary[i] + nums[i + 2];
                if (tmpSum > ary[i + 2])
                {
                    ary[i + 2] = tmpSum;
                }
                
                if (i + 3 < numsSize)
                {
                    tmpSum = ary[i] + nums[i + 3];
                    
                    if (tmpSum > ary[i + 3])
                    {
                        ary[i + 3] = tmpSum;
                    }
                }
            }
        }
        
        int maxNum = 0;
        
        if (ary[numsSize - 1] > ary[numsSize - 2])
        {
            return ary[numsSize - 1];
        }
        else
        {
            return ary[numsSize - 2];
        }
    }
}
