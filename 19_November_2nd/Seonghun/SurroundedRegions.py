from collections import deque

class Solution(object):
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])
        if rows < 3 or cols < 3:
            return
        
        for r in xrange(0,rows):
            if r > 0 and r < rows-1:
                self.traverse(board, r, 0, rows, cols)
                self.traverse(board, r, cols-1, rows, cols)
            else:
                for c in xrange(0,cols):
                    self.traverse(board, r, c, rows, cols)
                
        for r in xrange(0, rows):
            for c in xrange(0, cols):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
                
    def traverse(self, board, r, c, rows, cols):
        
        def hasZero(board, r, c, rows, cols):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == 'V' or board[r][c] == 'X':
                return False
            return True
        
        if hasZero(board, r, c, rows, cols) == False:
            return
        
        stack = deque()
        stack.append(r*cols + c)
        
        while (len(stack) > 0):
            val = stack.pop()
            r = val / cols
            c = val % cols
            
            board[r][c] = 'V'
            
            if hasZero(board, r+1, c, rows, cols):
                stack.append((r+1)*cols + c)
            if hasZero(board, r-1, c, rows, cols):
                stack.append((r-1)*cols + c)
            if hasZero(board, r, c+1, rows, cols):
                stack.append(r*cols + (c+1))
            if hasZero(board, r, c-1, rows, cols):
                stack.append(r*cols + (c-1))