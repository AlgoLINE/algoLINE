public class Solution {
    
    private static final int upperStart = 65; //A
    private static final int upperEnd = 90; //Z
    private static final int lowerStart = 97; //a
    private static final int lowerEnd = 122; //z
    private static final int numberStart = 48; //0
    private static final int numberEnd = 57; //9
    
    public boolean isPalindrome(String s) {
        int len = s.length();
        int lastIdx = len-1;
        int firstIdx = 0;

        while(firstIdx<lastIdx){
            char firstChar = s.charAt(firstIdx);
            char lastChar = s.charAt(lastIdx);
            
            //upper
            firstChar = convertToLower(firstChar);
            lastChar = convertToLower(lastChar);

            if(isAlphaOrNum(firstChar)){  
                if (isAlphaOrNum(lastChar)){
                    if(firstChar!=lastChar){
                        return false;
                    }else{
                        lastIdx--;
                        firstIdx++;
                        continue;
                    }
                }else{
                    lastIdx--;
                }
            } else {
                firstIdx++;
            }
        }
        return true;
    }
    
    private boolean isAlphaOrNum(char str){
        if((str>=lowerStart && str<=lowerEnd) || (str>=numberStart && str<=numberEnd))
            return true;
        else
            return false;
    }
    
    private char convertToLower(char str){
        if(str >= upperStart && str <= upperEnd)
            return (char)(str+32);
        else
            return str;
    }

}
