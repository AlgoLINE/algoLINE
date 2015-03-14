class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0
        source = x
        sign = 1
        
        if x < 0 :
            sign = -1
            source = ~x + 1
        
        while source is not 0 :
            result = result * 10
            result = result + (source % 10)
            source = source / 10
            
        result = sign * result
        
        if result > 2147483647 :
            return 0
        elif result < -2147483648 :
            return 0
            
        return result