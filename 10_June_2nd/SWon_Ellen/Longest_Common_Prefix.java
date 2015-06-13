public class Solution {
    public String longestCommonPrefix(String[] strs) {
        String compare = "";
        String prefix = "";
        int len = strs.length;
        int minLen = Integer.MAX_VALUE;
        
        for(int i=0; i<len; i++){
            int arrLen = strs[i].length();
            if(arrLen < minLen) {
                minLen = arrLen;
                compare = strs[i];
                prefix = strs[i];
            }
        }
        
        for(int i=0; i<len; i++){
            for(int j=0; j<minLen; j++){
                char strsPre = strs[i].charAt(j);
                char resPre = compare.charAt(j);
                if(strsPre!=resPre){
                    if(j==0)
                        prefix = "";
                    else
                        prefix = compare.substring(0, j);
                    minLen = prefix.length();
                    break;
                }
            }
        }
        
        if(prefix.length() < 0) 
            return "";
        else
            return prefix;
    }
}
