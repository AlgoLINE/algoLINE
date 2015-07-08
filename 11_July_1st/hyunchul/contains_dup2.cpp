class Solution {
public:
	bool containsNearbyDuplicate(vector<int>& nums, int k) {

		if (nums.size() < 1)
			return 0;

		map<int, int> dupMap;

		for (int i = nums.size() - 1; i >= 0; i--)
		{
			map<int, int>::iterator dupMapIndserIter;
			dupMapIndserIter = dupMap.find(nums[i]);
			if (dupMapIndserIter != dupMap.end())
			{
				if (dupMapIndserIter->second - i <= k)
				{
					return true;
				}
				else
				{
					dupMapIndserIter->second = i;
				}
			}
			else
			{
				dupMap.insert(pair<int, int>(nums[i], i));
			}
		}

		return false;

	}
};