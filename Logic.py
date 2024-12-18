import random

class SaperLogic:
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.place_bombs()
        self.calculate_neighbors()

    def place_bombs(self):
        bombs_placed = 0
        while bombs_placed < self.bombs:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:  # -1 oznacza bombê
                self.board[row][col] = -1
                bombs_placed += 1

    def calculate_neighbors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue
                self.board[row][col] = self.count_bombs(row, col)

    def count_bombs(self, row, col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                r, c = row + i, col + j
                if 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == -1:
                    count += 1
        return count

    def reveal(self, row, col):
        if self.revealed[row][col] or self.board[row][col] == -1:
            return False
        self.revealed[row][col] = True
        if self.board[row][col] == 0:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    r, c = row + i, col + j
                    if 0 <= r < self.rows and 0 <= c < self.cols:
                        self.reveal(r, c)
        return True

