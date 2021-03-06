class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if triangle is None :
            return 0
            
        rowCount = len(triangle)
        
        if rowCount == 0 :
            return 0
        
        table = [9223372036854775807] * rowCount
        
        table[0] = triangle[0][0]
        
        for rowIdx in range(1, rowCount) :
            eachRow = triangle[rowIdx]
            elementCount = len(eachRow)
            
            for eachIdx in range(0, elementCount - 1) :
                table[eachIdx] += eachRow[eachIdx]
            
            for eachIdx in range(1, elementCount) :
                crrIdx = elementCount - eachIdx
                tempValue = table[crrIdx - 1] - eachRow[crrIdx - 1] + eachRow[crrIdx]
                if table[crrIdx] > tempValue :
                    table[crrIdx] = tempValue
                    
        retVal = 9223372036854775807
        
        for eachVal in table :
            if retVal > eachVal :
                retVal = eachVal
                
        return retVal
            