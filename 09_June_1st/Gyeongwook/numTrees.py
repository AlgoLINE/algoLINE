class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        lookupTable = [None] * (n+1)
        lookupTable[0] = 1
        
        return self.subTrees(1, n, lookupTable)		
    	
    def subTrees(self, start, end, lookupTable):
        count = end - start + 1
        
        if lookupTable[count] is not None:
            return lookupTable[count]
        
        cases = 0
        for root in range(1, count+1):
            cases += self.subTrees(1, root-1, lookupTable) * self.subTrees(root+1, count, lookupTable)
        
        lookupTable[count] = cases
        return cases