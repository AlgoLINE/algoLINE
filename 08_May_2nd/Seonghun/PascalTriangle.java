public class Solution {
    public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> rowsList = new ArrayList<List<Integer>>();
        
        for (int row = 0 ; row < numRows ; row++) {
            
            List<Integer> rowList = new ArrayList<Integer>(row+1);
            
            for (int col = 0 ; col <= row ; col++) {
                
                if (col == 0 || col == row) 
                    rowList.add(1);
                else
                    rowList.add(rowsList.get(row-1).get(col-1) + rowsList.get(row-1).get(col));
            }
            
            rowsList.add(rowList);
        }
        
        return rowsList;
    }
}