class SolverOne:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        """Prints board for easier readability"""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - -")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(str(self.board[i][j]))
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def empty_find(self):
        """Returns the first empty position as a tuple of coordinates."""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)
        return

    def is_valid(self, pos, num):
        """Checks to see if the number is valid in the position that it is being tested.
                For example: If the column, row, and box contains the number 9, that position
                cannot be the number 9"""
        # column check
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # row check
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # box check
        x = pos[1] // 3
        y = pos[0] // 3
        for i in range(y * 3, y * 3 + 3):
            for j in range(x * 3, x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def bt_solve(self):
        """Solving the sudoku board with backtracking algorithm"""
        val = self.empty_find()
        if not val:
            return True
        else:
            row, col = val

        for i in range(1, 10):
            if self.is_valid((row, col), i):
                self.board[row][col] = i

                if self.bt_solve():
                    return True

                self.board[row][col] = 0

        return False
