class Solution {
public:
	int maximumGap(vector<int>& nums) {
		int length = nums.size();
		int maxGap = 0;

		radixSort32(nums, length);

		for (int idx = 1; idx < length; ++idx) {
			int currentGap = nums[idx] - nums[idx-1];
			maxGap = std::max(currentGap, maxGap);
		}

		return maxGap;
	}

private:
	void radixSort32(std::vector<int>& nums, int length) {
		std::vector<int> tempArray;
		tempArray.resize(length);

		std::array<int, 16> bucket;
		std::vector<int>* source = &nums;
		std::vector<int>* target = &tempArray;

		for (int sector = 0; sector < 32; sector += 4) {
			bucket.fill(0);
			for (int idx = 0; idx < length; ++idx) {
				++bucket[extractSectorBits(sector, (*source)[idx])];
			}

			for (int idx = 1; idx <= 0xF; ++idx) {
				bucket[idx] += bucket[idx-1];
			}

			for (int idx = length-1; idx >= 0; --idx) {
				(*target)[--bucket[extractSectorBits(sector, (*source)[idx])]] = (*source)[idx];
			}

			std::vector<int>* temp = source;
			source = target;
			target = temp;
		}
	}

	int extractSectorBits(int sectorPos, int number) {
		return 0xF & (number >> sectorPos);
	}
};