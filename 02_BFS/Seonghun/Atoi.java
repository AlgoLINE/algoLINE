public class Solution {

	// test
    
    private enum State{
        BEFORE,
        SIGN,
        INT
    }
    
    public int atoi(String str) {
        
        State state = State.BEFORE;
        
        char ch;
        
        int size = str.length();
        int idx = 0;
        int sign = 1;
        
        StringBuilder sb = new StringBuilder();
        
        while(idx < size){
            ch = str.charAt(idx);
            switch(state){
                case BEFORE:
                    if('0' <= ch && ch <= '9'){
                        sb.append(ch);
                        state = State.INT;
                    }
                    else if(ch == '+'){
                        sb.append(ch);
                        state = State.SIGN;
                    }
                    else if(ch == '-'){
                        sb.append(ch);
                        state = State.SIGN;
                        sign = -1;
                    }
                    else if(ch != ' '){
                        return 0;
                    }
                    break;
                case SIGN:
                    if('0' <= ch && ch <= '9'){
                        sb.append(ch);
                        state = State.INT;
                    }
                    else {
                        return 0;
                    }
                    break;
                case INT:
                    if('0' <= ch && ch <= '9'){
                        sb.append(ch);
                    }
                    else {
                        idx = size; // for escaping loop
                    }
                    break;
                default:
                    break;
            }
            idx++;
        }
        
        try{
            if(sb.length() > 0)   return Integer.parseInt(sb.toString());
            else                  return 0;    
        }
        catch(NumberFormatException e){ 
            return (sign == 1)? Integer.MAX_VALUE:Integer.MIN_VALUE;
        }
        
    }

}
