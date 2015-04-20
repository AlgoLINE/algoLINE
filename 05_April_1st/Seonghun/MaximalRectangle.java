public class Solution {
    public int maximalRectangle(char[][] matrix) {
        
        if(matrix.length == 0)  return 0;
        
        int col = matrix[0].length;
        int scan[] = new int[col];
        
        int max = 0;
        for(int row = 0 ; row < matrix.length ; row++){              // scan all rows
            // scan each element and cumulate
            for(int idx = 0 ; idx < col ; idx++){
                if(matrix[row][idx] == '1')  scan[idx]++;
                else                         scan[idx] = 0;
            }
            
            int arr[] = new int[matrix.length];
            for(int idx = 0 ; idx < scan.length ; idx++){
                for(int i = 0 ; i < arr.length ; i++){
                    if(i < scan[idx])   arr[i]++;
                    else                arr[i] = 0;
                }
                for(int i = 0 ; i < arr.length ; i++){
                    int val = (i+1)*arr[i];
                    if(val > max){
                        max = val;
                    }
                }
            }
            
        }
        
        return max;
    }
}