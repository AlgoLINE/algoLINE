public class Solution {
    public String countAndSay(int n) {
        String say = "1";
        StringBuilder str = new StringBuilder();

        for(int i = 1 ; i < n ; i++)
        {
            str.setLength(0);
            for( int j = 0 ; j < say.length() ; j++ )
            {
                char t = say.charAt(j);
                int count = 1;
                
                j++;
                
                while(j < say.length() && say.charAt(j) == t)
                {
                    count++;
                    j++;
                }
                
                j--;
                
                str.append(count);
                str.append(t);
            }
            say = str.toString();
        }
        
        return say;
    }
}