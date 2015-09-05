class Solution(object):
    def isAnagram(self, s, t):
        return True if ''.join(sorted(s)) == ''.join(sorted(t)) else False