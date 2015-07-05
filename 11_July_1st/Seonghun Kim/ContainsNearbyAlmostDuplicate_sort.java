public class Solution {
    
    static class IdxNode {
        
        public int value;
        public int idx;
        
        public IdxNode (int value, int idx) {
            this.value = value;
            this.idx = idx;
        }
    }
        
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        
        if (nums.length <= 1)
            return false;
            
        // make array    
        List<IdxNode> list = new ArrayList<IdxNode>(nums.length);
        for (int idx = 0 ; idx < nums.length ; idx++) {
            list.add(new IdxNode(nums[idx], idx));
        }
        
        // sort
        Collections.sort(list, new Comparator<IdxNode>() {
            public int compare(IdxNode o1, IdxNode o2) {
                if (o1.value < o2.value)
                    return -1;
                else if (o1.value > o2.value)
                    return 1;
                else
                    return 0;
            }
        });
        
        // find condition
        for (int i = 0 ; i < nums.length ; i++) {
            for (int j = i+1 ; j < nums.length ; j++) {
                
                int abs = Math.abs(list.get(i).value - list.get(j).value);
                if (abs < 0 || abs > t)
                    break;
                    
                if (Math.abs(list.get(i).idx - list.get(j).idx) <= k)
                    return true;
            }
        }
        return false;
    }
}