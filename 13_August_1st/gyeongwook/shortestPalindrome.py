class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        self.length = len(s)
        self.pivot = self.length
        
        while self.pivot > 1:
            self.left = self.pivot/2 - 1
            self.right = self.left+1 if self.pivot%2 == 0 else self.left+2
            
            while self.left >= 0 and self.right < self.length:
                if s[self.left] == s[self.right]:
                    self.left -= 1
                    self.right += 1
                else:
                    self.shift(s)
                    break
            		
            if self.left == -1:
                return s[:self.right+self.left:-1] + s
        
        return s[:0:-1] + s
        
    def shift(self, s):
        step = 0
        while True:
            self.pivot -= 1
            step += 1
            
            if self.pivot <= self.right+1 or self.pivot == 1 or s[self.left - step] == s[self.right]:
                break