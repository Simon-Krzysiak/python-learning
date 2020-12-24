"""Task:
    Implement an algorithm that will check whether the given grid of numbers
    represents a valid Sudoku puzzle. Note that the puzzle represented by
    grid does not have to be solvable.
"""


class Hist(dict):

    def count_digit(self, x):
        if x != '.':
            self[x] = self.get(x, 0)+1

    def check_valid(self):
        return max(self.values(), default=0) <= 1


def check_row(grid, row_index):
    digits = Hist()
    for j in range(9):
        digits.count_digit(grid[row_index][j])
    return digits.check_valid()


def check_column(grid, col_index):
    digits = Hist()
    for i in range(9):
        digits.count_digit(grid[i][col_index])
    return digits.check_valid()


def check_subgrid(grid, row_index, col_index):
    digits = Hist()
    for i in range(3):
        for j in range(3):
            digits.count_digit(grid[row_index+i][col_index+j])
    return digits.check_valid()


def sudoku2(grid):
    for row in range(9):
        if not check_row(grid, row):
            print('Row fail:', row)
            return False

    for col in range(9):
        if not check_column(grid, col):
            print('Column fail:', col)
            return False

    for i in range(3):
        for j in range(3):
            if not check_subgrid(grid, 3*i, 3*j):
                print('Subgrid fail:')
                print('row:', 3*i, 'column:', 3*j)
                return False

    return True
