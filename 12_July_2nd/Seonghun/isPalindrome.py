class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        
        l = 0
        r = len(s)-1
        s = s.lower()
        
        while True:
            # move left index if next character is not alphanumeric
            while l <= r and s[l].isalnum() == False:
                l += 1
            
            # move right index if next character is not alphanumeric
            while r >= l and s[r].isalnum() == False:
                r -= 1
            
            # if two indexes change
            if l > r:
                return True
            
            # if not palindrome
            if s[l] != s[r]:
                return False
            
            # move to next indexes
            l += 1
            r -= 1
            
        return True