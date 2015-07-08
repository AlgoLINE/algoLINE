class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        front = 0
        end = len(s)-1
        
        s = s.lower()
        
        while front < end:
            if not self.isAlphanumeric(s[front]):
                front += 1
                continue
            
            if not self.isAlphanumeric(s[end]):
                end -= 1
                continue
            
            if s[front] == s[end]:
                front += 1
                end -= 1
            else:
                return False
                
        return True
        
    def isAlphanumeric(self, c):
        return (c >= '0' and c <= '9') or (c >= 'a' and c <= 'z')