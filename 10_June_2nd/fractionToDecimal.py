class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        positive = True
        if numerator*denominator < 0:
            positive = False
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        integer = `(numerator / denominator)`
        remainder = numerator % denominator
        
        map = {}
        idx = -1
        cnt = 0
        decimalArray = []
        
        while remainder != 0:
            key = `remainder`;
            if map.has_key(key):        # check repeat
                idx = map[key]          # idx of repeated numbers
                break
            map[key] = cnt
            
            remainder *= 10
            quotient = `(remainder / denominator)`
            remainder = remainder % denominator
            decimalArray.append(quotient)
            cnt += 1
        
        val = []
        if positive == False:
            val.append('-')
            
        val.append(integer)
        if (idx != -1):             # if fractional part is repeated
            val.append('.')
            val.extend(decimalArray[:idx])
            val.append('(')
            val.extend(decimalArray[idx:])
            val.append(')')
        elif (cnt > 0):             # if fractional part is NOT repeated
            val.append('.')
            val.extend(decimalArray)
        
        return ''.join(val);