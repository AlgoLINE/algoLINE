class Solution {
public:
    int divide(int dividend, int divisor) {
        const int signMask = 0x80000000;
        
        const int sign = (signMask & dividend) ^ (signMask & divisor);
        
        unsigned int unsignedDividend = dividend;
        if ( unsignedDividend & signMask) {
            unsignedDividend = ~dividend;
            ++unsignedDividend;
        }
        
        unsigned int unsignedDivisor = divisor;
        if (divisor & signMask) {
            unsignedDivisor = ~divisor;
            ++unsignedDivisor;
        }
        
        unsigned int lowerBound = 0;
        unsigned int upperBound = unsignedDivisor;
        
        unsigned int lowerQuotient = 0;
        unsigned int upperQuotient = 1;
        
        unsigned int midBound = 0;
        unsigned int midQuotient = 0;
        
        while (upperBound < unsignedDividend) {
            lowerBound = upperBound;
            upperBound <<= 1;
            
            lowerQuotient = upperQuotient;
            upperQuotient <<= 1;
        }
        
        while (lowerQuotient != upperQuotient) {
            if (upperBound == unsignedDividend) {
                midQuotient = upperQuotient;
                break;
            } else if (lowerBound == unsignedDividend) {
                midQuotient = lowerQuotient;
                break;
            } 
            
            midBound = lowerBound + ((upperBound - lowerBound) >> 1);
            midQuotient = lowerQuotient + ((upperQuotient - lowerQuotient) >> 1);
            
            if (midBound < unsignedDividend) {
                lowerBound = midBound;
                lowerQuotient = midQuotient;
            } else if (midBound > unsignedDividend) {
                upperBound = midBound;
                upperQuotient = midQuotient;
            } else {
                break;
            }
        }
        
        if (midQuotient & signMask && !sign) {
            return INT_MAX;
        }
        
        return (sign) ? ~int(midQuotient) + 1 : int(midQuotient);
    }
};
