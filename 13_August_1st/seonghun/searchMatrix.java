public class Solution {
    
    private int[][] matrix;
    private int target;
    
    public boolean searchMatrix(int[][] matrix, int target) {
        this.matrix = matrix;
        this.target = target;
        
        return search(0, matrix.length-1, 0, matrix[0].length-1);
    }
    
    boolean search(int sr, int fr, int sc, int fc) {
        if (sr > fr)
            return false;
        if (sc > fc)
            return false;
        if (this.target < this.matrix[sr][sc] || this.target > this.matrix[fr][fc]) {
            return false;
        }
            
        int mr = (sr+fr)/2;
        int mc = (sc+fc)/2;
        int val = this.matrix[mr][mc];
        
        if (val == this.target)
            return true;
            
        if (this.target < val) {
            if (search(mr, fr, sc, mc-1))
                return true;
            if (search(sr, mr-1, mc, fc))
                return true;
            if (search(sr, mr-1, sc, mc-1))
                return true;
        } else {
            if (search(mr+1, fr, sc, mc))
                return true;
            if (search(sr, mr, mc+1, fc))
                return true;
            if (search(mr+1, fr, mc+1, fc))
                return true;
        }
        
        return false;
    }
}