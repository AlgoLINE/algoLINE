public class Solution {
    public String countAndSay(int n) {
        
        if (n == 0)
            return "";
        
        List<Integer> l = new ArrayList(1);
        l.add(1);
        
        for (int i = 1 ; i < n ; i++) {
            
            List<Integer> tempL = new ArrayList(l.size()*2);
            
            int cnt = 0;
            for (int j = 0 ; j < l.size() ; j++) {
                
                cnt++;
                
                if(j == l.size()-1 || (j < l.size()-1 && l.get(j) != l.get(j+1))) {
                    
                    tempL.add(l.get(j));
                    tempL.add(cnt);
                    cnt = 0;
                }
            }
            
            l = tempL;
        }
        
        StringBuilder sb = new StringBuilder(l.size());
        for (int i = l.size()-1 ; i >= 0 ; i--) {
            sb.append(l.get(i));
        }
        
        return sb.toString();
    }
}