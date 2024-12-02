import copy
from cell import Cell


class Grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid = [[Cell(x, y, 'E') for y in range(col)] for x in range(row)]
    def __deepcopy__(self, memo):
        new_grid = Grid(self.row, self.col)
        new_grid.grid = [[copy.deepcopy(cell) for cell in row] for row in self.grid]
        return new_grid
    def display_grid(self,grid):
        for row in grid:
            row_str = ' | '.join(str(cell) for cell in row)
            print(row_str)
            print('-' * len(row_str))

    def input_cell(self, x, y, cell_type):
        if 0 <= x < self.row and 0 <= y < self.col:
            self.grid[x][y] = Cell(x, y, cell_type)
