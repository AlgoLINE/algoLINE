public class Solution {
    public int longestConsecutive(int[] nums) {
        
        Set<Integer> values = new HashSet<Integer>();
        Set<Integer> set = new HashSet();
        int maxLength = 0;
        
        // put all values and their idx to hash map
        for (int value : nums) {
            values.add(Integer.valueOf(value));
        }
        
        Integer intObj = null;
        for (int i = 0 ; i < nums.length ; i++) {
            
            // for faster performance
            if (maxLength > (nums.length - i))
                return maxLength;
                
            int value = nums[i];
            
            // check duplicate values or already checked values
            intObj = Integer.valueOf(value);
            if (set.contains(intObj))
                continue;
            
            // add to set of checking duplicate number
            set.add(intObj);
            
            // variable for counting lenth from 'value'    
            int length = 0;
            
            // check adjacent left value 
            int copiedValue = value;
            intObj = Integer.valueOf(copiedValue);
            while (values.contains(intObj) != false) {
                set.add(intObj);
                length += 1;
                copiedValue -= 1;
                intObj = Integer.valueOf(copiedValue);
            }
            
            // check adjacent right value
            copiedValue = value+1;
            intObj = Integer.valueOf(copiedValue);
            while (values.contains(intObj) != false) {
                set.add(intObj);
                length += 1;
                copiedValue += 1;
                intObj = Integer.valueOf(copiedValue);
            }
            
            // compare currnet length with maxLength and update if currnet length is bigger
            if (length > maxLength) {
                maxLength = length;
            }
        }
        
        return maxLength;
    }
}