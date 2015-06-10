public class Solution {
    public List<Integer> grayCode(int n) {
        ArrayList<Integer> grayCode = new ArrayList<Integer>();
        grayCode.add(0);
        
        for(int i = 0 ; i < n ; i++)
        {
            int p = 1 << i;
            ArrayList<Integer> plusCode = (ArrayList<Integer>)grayCode.clone();
            Collections.reverse(plusCode);
            for( int j = 0 ; j < plusCode.size() ; j++)
            {
                grayCode.add(plusCode.get(j) + p);
            }
        }
        return grayCode;
        
    }
}