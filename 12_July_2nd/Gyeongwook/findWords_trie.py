class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        self.len_y = len(board)
        self.len_x = len(board[0])

        self.board = board
        self.words = words
        self.path = set()

        self.trie = {}
        self.return_val = []

        for each_word in words:
            node = self.trie

            for each_character in each_word:
                if not each_character in node:
                    node[each_character] = {}

                node = node[each_character]

            node['!'] = '!'

        for y in range(self.len_y):
            for x in range(self.len_x):
                self.path = set()
                self.search(x, y, '', self.trie)

        return self.return_val

    def search(self, x, y, prefix, node):
        if '!' in node:
            self.return_val.append(prefix)
            del node['!']

        if x < 0 or x >= self.len_x or y < 0 or y >= self.len_y:
            return

        if not (x, y) in self.path and self.board[y][x] in node:
            self.path.add((x, y))
            self.search(x+1, y, prefix+self.board[y][x], node[self.board[y][x]])
            self.search(x-1, y, prefix+self.board[y][x], node[self.board[y][x]])
            self.search(x, y+1, prefix+self.board[y][x], node[self.board[y][x]])
            self.search(x, y-1, prefix+self.board[y][x], node[self.board[y][x]])
            self.path.remove((x, y))
