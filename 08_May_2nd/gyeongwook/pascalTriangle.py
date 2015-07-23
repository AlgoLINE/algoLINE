class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0 : return []
        
        triangle = []
        triangle.append([1])
        
        for length in range(2, numRows+1) :
            current_row = []
            
            for idx in range(length) :
                left = triangle[length-2][idx-1] if idx != 0 else 0
                right = triangle[length-2][idx] if idx != length-1 else 0
                current_row.append(left + right)  
                
            triangle.append(current_row)
            
        return triangle