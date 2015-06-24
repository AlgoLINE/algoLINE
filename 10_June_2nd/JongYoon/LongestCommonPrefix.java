public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        else if (strs.length == 1)
            return strs[0];
        
        int prefixNum = strs[0].length() - 1;
        int prefix = -1;
        
        for( int i = 1 ; i < strs.length ; i++)
        {
            prefix = -1;
            
            for(int j = 0 ; j <= prefixNum && j < strs[i].length() && j < strs[i-1].length() ; j++ )
            {
                if(strs[i-1].charAt(j) == strs[i].charAt(j)) prefix = j;
                else break;
            }
            
            if ( prefix == -1 )
                return "";
                
            prefixNum = prefix;
        }
       
        return strs[0].substring(0,prefixNum+1);
    }
}