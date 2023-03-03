
class Board:
    def __init__(self):
        self.board_size = int(input("Entrez la taille de la board: "))
        self.board = []
        for x in range(1, self.board_size+1):
            self.col = []
            for y in range(1, self.board_size+1):
                self.col.append("O")
            self.board.append(self.col)
        self.x = 0
        self.y = 0
        self.loop = True
        self.gen_queen(self.x, self.y)
        self.show_board()

    def show_board(self):
        for i in self.board:
            print(' '.join(i))
    
    def gen_queen(self, x, y):
        if y > self.board_size - 1:
            y = 1
        if x == self.board_size:
            self.loop = False
        
        if self.loop:
            self.board[x][y] = 'X'
            self.gen_queen(x + 1, y + 2)

board = Board()
