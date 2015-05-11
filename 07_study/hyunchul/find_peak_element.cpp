class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int count = nums.size();
        int half = count / 2;
        int prevHalf = 0;
        int state = 0;
        int retIndex = 0;
        
        if (nums.size() == 1)
        {
            return 0;
        }
        else if (nums.size() == 2)
        {
            if (nums[0] > nums[1])
            {
                return 0;
            }
            else
            {
                return 1;
            }
        }
        
        while (1)
        {
            if (state != 0)
            {
                if (half == count - 1 || half == 0)
                {
                    return half;
                }
            }
            
            if (nums[half] < nums[half + 1])
            {
                if ((half + 2) < count && nums[half + 1] > nums[half + 2])
                {
                    retIndex = half + 1;
                    break;
                }
                else
                {
                    if (state == 0)
                    {
                        state = 1;
                        if ((count - half) / 2 == 0)
                        {
                            half += 1;
                        }
                        else
                        {
                            half += (count - half) / 2;
                        }
                    }
                    else if (state == 1)
                    {
                        if (((count -half) / 2)  == 0)
                        {
                            half += 1;
                        }
                        else
                        {
                            half += (count - half) / 2;
                        }
                    }
                    else if (state == -1)
                    {
                        if ((half - prevHalf) / 2 == 0)
                        {
                            half += 1;
                        }
                        else
                        {
                            half += ((half - prevHalf) / 2);
                        }
                        state = -1;
                    }
                }
            }
            else if (nums[half] > nums[half + 1])
            {
                if (half - 1 >= 0 && nums[half - 1] < nums[half])
                {
                    retIndex = half;
                    break;
                }
                else
                {
                    if (state == 0)
                    {
                        state = -1;
                        if (half / 2 == 0)
                        {
                            half -= 1;
                        }
                        else
                        {
                            half -= (half / 2);
                        }
                    }
                    else if (state == -1)
                    {
                        if (half / 2 == 0)
                        {
                            half -= 1;
                        }
                        else
                        {
                            half -= (half / 2);
                        }
                    }
                    else if (state == 1)
                    {
                        if ((prevHalf -half) / 2 == 0)
                        {
                            half -= 1;
                        }
                        else
                        {
                            half -= ((prevHalf -half) / 2); 
                        }
                        state = 1;
                    }

                }
            }
            prevHalf = half;
        }
        
        return retIndex;
    }
};