class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        self.column_len = len(board)
        self.row_len = len(board[0])
        self.board = board
        self.words = words
        self.path = set()
        
        return_val = []
        
        for each_word in words:
            if self.retrieve(each_word):
                return_val.append(each_word)
            
        return return_val
        
    def retrieve(self, each_word):
        self.path = set()
        
        for column in range(self.column_len):
            for row in range(self.row_len):
                if each_word[0] == self.board[column][row] and self.move(each_word, 0, column, row):
                    return True
        
        return False

    def move(self, word, idx, current_column, current_row):
        current_position = (current_row, current_column)
        self.path.add(current_position)
        
        if self.next_step(word, idx+1, current_column, current_row-1):
            return True
        	
        if self.next_step(word, idx+1, current_column, current_row+1):
            return True
        
        if self.next_step(word, idx+1, current_column-1, current_row):
            return True
        
        if self.next_step(word, idx+1, current_column+1, current_row):
            return True
        
        self.path.remove(current_position)
        return False
    
    def next_step(self, word, idx, current_column, current_row):
        if idx >= len(word):
            return True
            
        if current_column >= self.column_len or current_column < 0 or current_row >= self.row_len or current_row < 0:
            return False
        
        if (current_row, current_column) in self.path:
            return False
        
        if self.board[current_column][current_row] == word[idx]:
            return self.move(word, idx, current_column, current_row)
        
        return False