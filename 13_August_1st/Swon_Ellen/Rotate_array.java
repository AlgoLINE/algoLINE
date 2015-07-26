public class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        int res[] = new int[len];
        
        if(len==k) return; // worst case
        
        k = k%len;
        
        for(int i=0; i<k; i++){
            res[i] = nums[len-k+i];
        }
        for(int i=0; i<len-k; i++){
            res[k+i] = nums[i];
        }
        for(int i=0; i<len; i++){
            nums[i]=res[i];
        }
    }
}
