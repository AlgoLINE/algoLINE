class Solution:
    # @return an integer
    def atoi(self, str):
        strLen = len(str)
        
        if strLen == 0 :
            return 0
            
        sign = 1
        startPos = 0
        result = 0
        
        while str[startPos] == ' ' :
            startPos = startPos + 1
        
        if str[startPos] == '-' or str[startPos] == '+' :
            if str[startPos] == '-' :
                sign =  sign * -1
                
            startPos = startPos + 1
            
        for idx in range(startPos, strLen) :
            if str[idx] < '0' or str[idx] > '9' :
                result = sign * result
                if result > 2147483647 :
                    return 2147483647
                elif result < -2147483648 :
                    return -2147483648
                return result
            
            result = result * 10
            result = result + int(str[idx])
            
        
        result = sign * result
        if result > 2147483647 :
            return 2147483647
        elif result < -2147483648 :
            return -2147483648
        return result