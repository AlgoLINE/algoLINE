class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		map<int, int> valMap;

		vector<int> resultVector;

		for (int i = 0; i < nums.size(); i++)
		{
			valMap.insert(pair<int, int>(nums[i], i));
		}

		for (int i = 0; i < nums.size(); i++)
		{
			int subTarget = target - nums[i];
			map<int, int>::iterator iter = valMap.find(subTarget);

			if (iter != valMap.end())
			{
				if (iter->second == i)
				{
					continue;
				}

				if (iter->second < i)
				{
					resultVector.push_back(iter->second + 1);
					resultVector.push_back(i + 1);
				}
				else
				{
					resultVector.push_back(i + 1);
					resultVector.push_back(iter->second + 1);
				}
				break;
			}
		}

		return resultVector;
	}
};