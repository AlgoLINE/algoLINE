public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        StringBuilder num = new StringBuilder();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sign = 1;
        
        if( numerator == 0 || denominator == 0)
            return "0";
        
        if( numerator < 0 )
        {
            numerator *= -1;
            sign *= -1;
        }
        
         if( denominator < 0 )
        {
            denominator *= -1;
            sign *= -1;
        }
        
        if( sign < 0 )
            num.append('-');
        
        int rNum = devision( numerator, denominator, num);
        if( rNum == 0 ) return num.toString();
        
        num.append('.');
        map.put(rNum, num.length());
        rNum *= 10;
        
        while(true)
        {
            if( rNum < denominator ) {
                rNum *= 10;
                num.append('0');
                continue;
            }

            if(map.containsKey(rNum))
            {
                int l = map.get(rNum);
                num.append(')');
                num.insert(l, '(');
                break;
            }
            
            map.put(rNum, num.length());
            rNum = devision( rNum, denominator, num);
            rNum *= 10;
            
            if( rNum == 0 ) return num.toString();
        }
        
        return num.toString();
    }
    
    int devision( int numerator, int denominator, StringBuilder num)
    {
        int iNum = numerator / denominator;
        int rNum = numerator % denominator;
        
        num.append(iNum);
        return rNum;
    }
}