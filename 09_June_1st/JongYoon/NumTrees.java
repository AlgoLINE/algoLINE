public class Solution {
    public int numTrees(int n) {
        int[] num = new int[n];
        num[0] = 1;
        
        for( int i = 1 ; i < n ; i++)
        {
            num[i] = 0;
            int cnt = (i+1)/2;
            
            if( (i+1) % 2 == 1 )
                num[i] += num[cnt - 1] * num[cnt - 1];
            
            num[i] += num[i-1] * 2;  
            
            for( int j = 2 ; j <= cnt ; j++)
            {
                num[i] += num[i-j] * num[j-2] * 2;
            }
        }
        
        return num[n-1];
    }
}