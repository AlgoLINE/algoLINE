class Solution(object):
    def minCut(self, s):
        self.length = len(s)
        self.table = [[-1 for x in range(self.length)] for x in range(self.length)]
        
        # -1 : not visited
        # 0 : not palindrome
        # 1: palindrome
        
        for idx in range(0,self.length):
            self.table[idx][idx] = 1
        
        for length in range(2,self.length+1):
            for start in range(self.length-length+1):
                end = start + length - 1
                if length > 2 and self.table[start+1][end-1] == 0:
                    self.table[start][end] = 0
                elif s[start] == s[end]:
                    self.table[start][end] = 1
                else:
                    self.table[start][end] = 0
        
        self.lookup = [None for x in range(self.length)]
        
        return self.search(0)-1
            
    def search(self, start):
        if start == self.length: return 0
        if self.lookup[start] is not None: return self.lookup[start]
        
        cut = self.length-start-1
        for end in range(start, self.length):
            if self.table[start][end] == 1:
                cut = min(cut, self.search(end+1))
        
        self.lookup[start] = cut+1
        return cut+1