public class Solution {
    public int divide(int dividend, int divisor) {
        
        // check overflow
        if(dividend == Integer.MIN_VALUE && divisor == -1)                  
            return Integer.MAX_VALUE;
        
        // return simple value
        if(divisor == 1)                return dividend;
        if(divisor == -1)               return ~dividend +1;
        if((dividend^divisor) == 0)     return 1;               // equal
        if((~(dividend^divisor)) == 1)  return -1;              //
        
        // determine sign of result
        boolean neg = ((dividend^divisor) < 0);
        
        // convert to negative values because negative value has +1 value.
        if(dividend > 0) dividend = ~dividend + 1;
        if(divisor > 0)  divisor = ~divisor + 1;
        
        int tDividend = dividend;
        int q = 0;
        while(divisor > tDividend){
            
            int mul = 1;
            int tDivisor = divisor;
            int nextShift = (tDivisor << 1);
            while(nextShift < 0 && nextShift >= tDividend){
                mul = mul << 1;                     // update multiplier
                tDivisor = nextShift;               // save current shift value to tDivisor
                nextShift = nextShift << 1;         // move to next shift
            }
            
            q += mul;                               // add current multiplier to quotient
            tDividend -= tDivisor;                  // set tDividend to remainder 
            
        }
        
        if(neg) return ~q + 1;
        return q;
        
    }
    
}