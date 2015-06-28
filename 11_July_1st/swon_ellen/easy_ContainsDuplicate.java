public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int len = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i=0; i<len; i++){
            Integer num = new Integer(nums[i]);
            Integer map_get = map.get(num);
            
            if(map_get!=null){ 
                if(i-map_get <= k){ 
                    return true;
                }else{
                    map.remove(num, map_get);
                    map.put(num, new Integer(i));
                }
            }else{
                map.put(num, new Integer(i));
            }
        }
        return false;
    }
}
