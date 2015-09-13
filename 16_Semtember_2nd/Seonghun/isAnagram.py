class Solution(object):
    def isAnagram(self, s, t):
        
        leng = len(s)
        if leng != len(t):
            return False
        
        mapper = [0] * 26
        norm = ord('a')
        
        for idx in xrange(0,leng):
            c1 = ord(s[idx])-norm
            c2 = ord(t[idx])-norm
            
            mapper[c1] += 1
            mapper[c2] -= 1
                
        for value in mapper:
            if value != 0:
                return False
        return True