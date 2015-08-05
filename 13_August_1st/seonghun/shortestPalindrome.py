class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        idx = 0
        rIdx = len(s)-1
        addIdx = rIdx
        pre = []
        
        def partPalindrome(idx, rIdx):
            while idx >= 0:
                if s[idx] != s[rIdx]:
                    return False
                idx -= 1
                rIdx += 1
            return True
        
        while idx <= rIdx:
            if s[idx] != s[rIdx]:
                while partPalindrome(idx, rIdx) == False:
                    pre.append(s[addIdx])
                    addIdx -= 1
                    idx -= 1
            idx += 1
            rIdx -= 1
        
        for ch in s:
            pre.append(ch)
        return ''.join(pre)