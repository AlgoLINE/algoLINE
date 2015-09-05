class Solution(object):
    def isAnagram(self, s, t):
        lookup_table = [0] * 26
        
        for each in s:
            lookup_table[ord(each)-ord('a')] += 1
            
        for each in t:
            lookup_table[ord(each)-ord('a')] -= 1
            
        for each in lookup_table:
            if each != 0: return False
            
        return True