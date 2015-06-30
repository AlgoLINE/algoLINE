package algoLine;

/**
 * 
 * @author yejin-kim
 *
 */
public class EASY_ContainsDuplicateSolution {
	public boolean containsNearbyDuplicate(int[] nums, int k) {
		/** if length is less than 2, there is no room to compare **/
        if (nums.length < 2) {
            return false;
        }
        /** 1) set range of benchmark **/
        int bigLimit = nums.length > k ? nums.length - k : nums.length;
        for (int i = 0 ; i < bigLimit ; i++) {
        	/** 2) set range of comparator **/
            int smallLimit = i + k + 1 > nums.length ? nums.length : i + k + 1;
            for (int j = i + 1 ; j < smallLimit; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}
