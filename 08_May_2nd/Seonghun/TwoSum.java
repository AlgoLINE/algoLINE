public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        if (nums == null || nums.length < 2)
            return null;
        
        int leng = nums.length;
        Map<Integer, Integer> numIdxMap = new HashMap<Integer, Integer>();
        
        for (int i = 0 ; i < leng ; i++) {
            
            int diff = target - nums[i];
            
            if (numIdxMap.containsKey(diff)) {
                
                int prvIdx = numIdxMap.get(diff);
                
                int[] result = new int[2];
                if (i < prvIdx) {
                    result[0] = i+1;
                    result[1] = prvIdx+1;
                } else {
                    result[0] = prvIdx+1;
                    result[1] = i+1;
                }
                
                return result;
            }
            
            numIdxMap.put(nums[i], i);
        }
        
        return null;
    }
}