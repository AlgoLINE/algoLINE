class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        sign = '' if (numerator>=0 and denominator>=0) or (numerator<=0 and denominator<=0) > 0 else '-'
        
        numerator = numerator if numerator > 0 else -numerator
        denominator = denominator if denominator > 0 else -denominator
        
        return_val = str(numerator/denominator)
        rest_part = ""
        
        point_pos = len(return_val)
        current_numerator = numerator%denominator
        
        if current_numerator != 0:
            return_val += '.'
            
            index = 0
            loop_table = {}
            
            while current_numerator != 0:
                current_numerator *= 10
                
                if current_numerator in loop_table:
                    return_val += rest_part[0:loop_table[current_numerator]] 
                    return_val += '(' + rest_part[loop_table[current_numerator]:] + ')'
                    return sign + return_val
                
                loop_table[current_numerator] = index
                rest_part += str(current_numerator/denominator)
                
                current_numerator = current_numerator%denominator
                index += 1
        
        return sign + return_val + rest_part
                