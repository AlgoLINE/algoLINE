public class Solution {
    StringBuilder result;
    StringBuilder tmp;
    char prev = 1;
    int count = 1;
    int len = 0;
    
    public String countAndSay(int n) {
        if(n==1)
            return "1";
            
        result = new StringBuilder("1");
        tmp = new StringBuilder();
        
        for (int i=1; i<n; i++) {
            len = result.length(); // hell
            prev = result.charAt(0);
            tmp.setLength(0);
            tmp.append(result.toString());
            result.setLength(0);
            
            for(int j=0; j<len; j++){
                if(j+1>=len){ // bound
                    attach();
                    break;
                }
                if(prev == tmp.charAt(j+1)){ // same
                    count++;
                }else{ // diff
                    attach();
                }
                if(j!=len-1)
                    prev = tmp.charAt(j+1);
            }
        }
        return result.toString();
    }
    void attach(){
        result.append(count);
        result.append(prev);
        count = 1;
    }
}

