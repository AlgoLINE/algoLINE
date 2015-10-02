class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
            
        list = [30, 15, 10, 6, 5, 3, 2]
        
        for item in list:
            while num % item == 0:
                num /= item
        
        if num > 1:
            return False
            
        return True