public class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length())
            return false;
        
        s = sort(s);
        t = sort(t);
        
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) != t.charAt(i))
                return false;
        }
        return true;
    }
    
    String sort(String str){
        char[] tmp = new char[str.length()];
        tmp = str.toCharArray();
        Arrays.sort(tmp);
        return str = String.valueOf(tmp);
    }
}
