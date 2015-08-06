class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        
        def search(sr, fr, sc, fc):
            if sr > fr or sc > fc:          # boundary check
                return False
                
            if target >= matrix[sr][sc] and target <= matrix[fr][fc]:
                
                mr = (sr+fr)/2
                mc = (sc+fc)/2
                val = matrix[mr][mc]
                
                if val == target:
                    return True
                if target < val:
                    if search(mr, fr, sc, mc-1) or search(sr, mr-1, mc, fc) or search(sr, mr-1, sc, mc-1):
                        return True
                if target > val:
                    if search(mr+1, fr, sc, mc) or search(sr, mr, mc+1, fc) or search(mr+1, fr, mc+1, fc):
                        return True;
                
            return False
            
        return search(0, len(matrix)-1, 0, len(matrix[0])-1)