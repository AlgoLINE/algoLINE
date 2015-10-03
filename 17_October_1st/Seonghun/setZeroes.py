class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if (row == 0):
            return
        col = len(matrix[0])
        
        colStatus = set()
        
        # change each row if it has zero at the same time write status of the value of each column
        for rIdx in xrange (0, row):
            rowHasZero = False
            for cIdx in xrange (0, col):
                if matrix[rIdx][cIdx] == 0:
                    colStatus.add(cIdx)
                    rowHasZero = True
                
            # if this row has zero, then change all elements in this row to zero
            if rowHasZero:
                for cIdx in xrange (0, col):
                    matrix[rIdx][cIdx] = 0
                    
        # for all the column which has zero, change all elements in the column to zero
        for cIdx in colStatus:
            for rIdx in xrange (0, row):
                matrix[rIdx][cIdx] = 0