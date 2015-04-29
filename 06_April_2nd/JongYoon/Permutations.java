public class Solution {
    List<Integer> permutation = new ArrayList<Integer>();
    List<List<Integer>> p = new ArrayList<List<Integer>>();
    
    public List<List<Integer>> permute(int[] num) {
    
        ArrayList<Integer> intList = new ArrayList<Integer>();
        for (int index = 0; index < num.length; index++)
        {
            intList.add(num[index]);
        }
        permutations(intList, intList.size());
        return p;
    }
    
    void permutations( ArrayList<Integer> num, int size)
    {
        if( size <= 0)
        {
            p.add(cloneList(permutation));
            return;
        }
        
        HashSet<Integer> set = new HashSet<Integer>();
      
        for(int i = 0 ; i < size; i++)
        {
            Integer pNum = num.get(i);
            if(set.contains(pNum))
                continue;
            set.add(pNum);
            permutation.add(pNum);
            Collections.swap(num, i, size - 1);
            permutations(num, size - 1);
            Collections.swap(num, i, size - 1);
            permutation.remove(permutation.size() -1);
        }
        
    }
    
    public List<Integer> cloneList(List<Integer> list) {
        List<Integer> clone = new ArrayList<Integer>(list.size());
        for(Integer item: list) clone.add(item);
        return clone;
    }
}
