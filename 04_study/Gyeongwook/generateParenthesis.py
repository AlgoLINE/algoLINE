class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        recordTable = {}
        recordTable[0] = ['']
        
        for count in range(1, n + 1) :
            currentList = set()
            for each in recordTable[count-1] :
                currentList.add('(' + each + ')')
                
            for subsetLen in range(1, count) :
                for part1 in recordTable[subsetLen] :
                    for part2 in recordTable[count-subsetLen] :
                        currentList.add(part1 + part2)
                        
            recordTable[count] = currentList
                            
        return list(recordTable[n])