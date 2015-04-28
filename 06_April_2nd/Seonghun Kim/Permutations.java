public class Solution {
    public List<List<Integer>> permute(int[] num) {
        
        if (num.length == 0) 
            return null;
        
        return permute(num, 0);
            
    }
    
    private List<List<Integer>> permute(int[] num, int idx){
        
        // condition for escaping recursion
        List<List<Integer>> newPerm = new LinkedList<List<Integer>>();
        if (idx == num.length-1) {
            List<Integer> list = new ArrayList<Integer>(1);
            list.add(num[idx]);
            newPerm.add(list);
            return newPerm;
        }
        
        int curItem = num[idx];
        List<List<Integer>> oldPerm = permute(num, idx+1);
        
        // concept : insert curItem into each empty space such as between, front or end of oldList.
        for (List<Integer> oldList : oldPerm) {
            for (int i = -1 ; i < oldList.size(); i++) {
                List<Integer> newList = new ArrayList<Integer>(num.length - idx);
                // -1 means that curItem should be inserted at front
                if (i == -1) {
                    newList.add(curItem);
                    newList.addAll(oldList);
                } else {
                    for (int j = 0 ; j < oldList.size() ; j++) {
                        newList.add(oldList.get(j));
                        if (i == j) {
                            newList.add(curItem);
                        }
                    }
                }
                newPerm.add(newList);
            }
        }
        
        return newPerm;
        
    }
    
}