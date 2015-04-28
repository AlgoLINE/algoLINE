public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        
        final int NUM_RESULT_SET = 2;
        int rows = triangle.size();
        int[][] result = new int[NUM_RESULT_SET][rows];
        
        int updateIdx = 1, originIdx = 0;
        int min = Integer.MAX_VALUE;
        
        result[originIdx][0] = triangle.get(0).get(0);
        
        for (int i = 0 ; i < rows-1 ; i++) {

            // leftmost            
            result[updateIdx][0] = result[originIdx][0] + triangle.get(i+1).get(0);
            
            // middle
            for (int j = 1 ; j <= i ; j++) {
                result[updateIdx][j] = Math.min(result[originIdx][j-1], result[originIdx][j]) + triangle.get(i+1).get(j);
            }
            
            // rightmost
            result[updateIdx][i+1] = result[originIdx][i] + triangle.get(i+1).get(i+1);
            
            updateIdx = (updateIdx + 1) % NUM_RESULT_SET;
            originIdx = (originIdx + 1) % NUM_RESULT_SET;
        }
        
        
        for (int val : result[originIdx]) {
            if (val < min)
                min = val;
        }
        
        return min;
    }
}