class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        lookupTable = [None] * (n+1)
        lookupTable[0] = 1
        
        for count in range(1, n+1):
            cases = 0
            for root in range(count):
                cases += lookupTable[root] * lookupTable[count-root-1]
            
            lookupTable[count] = cases
        
        return lookupTable[n]