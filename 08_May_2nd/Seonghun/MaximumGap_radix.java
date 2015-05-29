public class Solution {
    public int maximumGap(int[] nums) {
        
        if (nums.length < 2)
            return 0;
            
        final int cipher = 9,
            digit = 10,
            len = nums.length;
        
        int[] counts = new int[digit];
        
        // start from lowest cipher to hightest one
        for (int i = 0 ; i < cipher ; i++) {
            
            int[] temp = new int[len];
            
            // initialize counts array
            for (int j = 0 ; j < digit ; j++) {
                counts[j] = 0;
            }
            
            // extract the value at the current cipher and use it as index for counting
            int divisor = (int) Math.pow(digit, i);
            for (int j = 0 ; j < len ; j++) {
                int idx = (nums[j] / divisor) % digit;
                counts[idx]++;
            }
            
            // accumulate counts
            for (int j = 1 ; j < digit ; j++) {
                counts[j] += counts[j-1];
            }
            
            // choose the position of each value at current phase (or cipher)
            for (int j = len-1 ; j >= 0 ; j--) {
                int idx = (nums[j] / divisor) % digit;
                temp[counts[idx]-1] = nums[j];
                counts[idx] -= 1;
            }
           
            // change reference
            nums = temp;
        }
            
        int diff = 0;
        for (int i = 1 ; i < len ; i++) {
            int temp = (int) Math.abs(nums[i] - nums[i-1]);
            if (temp > diff)
                diff = temp;
        }
        
        return diff;
    }
}