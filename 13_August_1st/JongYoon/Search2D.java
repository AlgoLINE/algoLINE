public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        
        return search(0, 0, matrix, target, row, col);
    }
    
    public boolean search(int row, int col, int[][] matrix, int target, int rowSize, int colSize) {
        
        if (row > rowSize || col > colSize)
            return false;
        
        int rowPos, colPos;
        
        for ( colPos = col ; colPos < colSize && matrix[0][colPos] <= target ; colPos++ );
        
        if (matrix[0][colPos] == target) {
            return true;
        }
        
        for (rowPos = row ; rowPos < rowSize && matrix[rowPos][colPos] <= target ; rowPos++)
        {
            if (matrix[rowPos][colPos] == target) {
                return true;
            }
        }
        if (rowPos == rowSize) {
            rowPos -= 1;
        }
        if (colPos != 0 ) {
            colPos -= 1;
        }     
        
        for ( ; colPos >= 0 && matrix[rowPos][colPos] >= target ; colPos-- ) {
            if (matrix[rowPos][colPos] == target) {
                return true;
            }
        }
        
        return search(rowPos+1, colPos, matrix, target, row, col);
    }
}