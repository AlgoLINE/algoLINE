public class Solution {
    
    static class IdxNode {
        
        public int value;
        public int idx;
        public IdxNode r;
        public IdxNode l;
        
        public IdxNode (int value, int idx) {
            this.value = value;
            this.idx = idx;
        }
    }
        
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        
        if (nums.length <= 1)
            return false;
            
        // make BST    
        IdxNode root = new IdxNode(nums[0], 0);
        for (int idx = 1 ; idx < nums.length ; idx++) {
            addIdx(root, nums[idx], idx);
        }
        
        // make sorted array
        List<IdxNode> list = new ArrayList<IdxNode>(nums.length);
        inorder(root, list);
        
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
    
    private void inorder(IdxNode root, List<IdxNode> nodes) {
        
        if (root != null) {
            inorder(root.l, nodes);
            nodes.add(root);
            inorder(root.r, nodes);
        }
    }
    
    private void addIdx (IdxNode node, int value, int idx) {
        
        if (node != null) {
            // add to BST
            while (node != null) {
                IdxNode parent = node;
                if (node.value < value) {           // move right from node
                    node = node.r;
                    if (node == null)
                        parent.r = new IdxNode(value, idx);
                } else {                             // move left from node
                    node = node.l;
                    if (node == null)
                        parent.l = new IdxNode(value, idx);
                }
            }
        }
    }
}