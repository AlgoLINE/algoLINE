class Solution(object):
    def solve(self, board):
        self.row_count = len(board)
        if self.row_count < 3: return
    
        self.column_count = len(board[0])
        if self.column_count < 3: return
    
        # upper
        for column_idx in range(self.column_count):
            if board[0][column_idx] == 'O':
                self.bfs(0, column_idx, board)
        
        # lower
        for column_idx in range(self.column_count):
            if board[self.row_count-1][column_idx] == 'O':
                self.bfs(self.row_count-1, column_idx, board)
        
        # left
        for row_idx in range(self.row_count):
            if board[row_idx][0] == 'O':
                self.bfs(row_idx, 0, board)
        
        # right
        for row_idx in range(self.row_count):
            if board[row_idx][self.column_count-1] == 'O':
                self.bfs(row_idx, self.column_count-1, board)
        
        for row_idx in range(self.row_count):
            for column_idx in range(self.column_count):
                if board[row_idx][column_idx] == 'O':
                    board[row_idx][column_idx] = 'X'
                elif board[row_idx][column_idx] == 'V':
                    board[row_idx][column_idx] = 'O'
        
    def bfs(self, row_idx, column_idx, board):
        queue = []
        
        board[row_idx][column_idx] = 'V'
        queue.append((row_idx, column_idx))
        
        while len(queue) > 0:
            (current_row_idx, current_column_idx) = queue.pop()
            
            if current_row_idx-1 >= 0 and board[current_row_idx-1][current_column_idx] == 'O':
                board[current_row_idx-1][current_column_idx] = 'V'
                queue.append((current_row_idx-1, current_column_idx))
                
            
            if current_row_idx+1 < self.row_count and board[current_row_idx+1][current_column_idx] == 'O':
                board[current_row_idx+1][current_column_idx] = 'V'
                queue.append((current_row_idx+1, current_column_idx))
                
            
            if current_column_idx-1 >= 0 and board[current_row_idx][current_column_idx-1] == 'O':
                board[current_row_idx][current_column_idx-1] = 'V'
                queue.append((current_row_idx, current_column_idx-1))
                
            
            if current_column_idx+1 < self.column_count and board[current_row_idx][current_column_idx+1] == 'O':
                board[current_row_idx][current_column_idx+1] = 'V'
                queue.append((current_row_idx, current_column_idx+1))