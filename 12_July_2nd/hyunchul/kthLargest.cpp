class Solution {
public:
	int findKthLargest(vector<int>& nums, int k) {
		if (nums.size() < 1)
			return 0;

		vector<int>::iterator firstIter = nums.begin();
		vector<int>::iterator lastIter = nums.end();
		sort(firstIter, lastIter, greater<int>());
		return nums[k - 1];
	}
};