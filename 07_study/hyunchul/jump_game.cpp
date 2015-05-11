class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> zeroIndexVector;
        int loopStartIndex = 0;
        int prevLoopStartIndex = -1;
        bool retFlag = false;
        int loopCount = 0;
        
        if (nums.size() == 1)
        {
            return true;
        }
        
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                zeroIndexVector.push_back(i);
            }
        }
        
        if (zeroIndexVector.size() < 1)
        {
            return true;
        }
        
        for (int i = 0; i < zeroIndexVector.size(); i++)
        {
            loopStartIndex = zeroIndexVector[i];
            for (int j = loopStartIndex; j > -1; j--)
            {
                if (nums[j] > (loopStartIndex - j))
                {
                    retFlag = true;
                    break;
                }
                
                if(j + nums[j] >= nums.size() - 1)
                {
                    return true;
                }
            }
            
            if(!retFlag)
            {
                return false;
            }
            
            if (i != zeroIndexVector.size() - 1)
                retFlag = false;
        }
        
        return retFlag;
        
    }
};