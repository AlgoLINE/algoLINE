class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        len_y = len(matrix)
        len_x = len(matrix[0])
        
        x = len_x-1
        y = 0
        
        while x >= 0 and y < len_y:
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                return True
            
        return False
        