import copy
import random
from cell import Cell
from grid import Grid
from movement import Movement


class DFS:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.movement = Movement()
        self.stack = [self.grid]  
        self.visited = set()

    def search(self):
        while self.stack:  
            current_grid = self.stack.pop() 

            current_grid_state = self.grid_to_hash(current_grid)

            if current_grid_state in self.visited:
                continue

            self.visited.add(current_grid_state)

            possible_moves = self.movement.get_possible_moves(current_grid)

            for target_cell in possible_moves:
                selected_cell = None
                possible_cells = []

                for x in range(current_grid.row):
                    for y in range(current_grid.col):
                        if current_grid.grid[x][y].type in ['p', 'wp', 'r', 'wr']:
                            possible_cells.append(current_grid.grid[x][y])

                if possible_cells:
                    selected_cell = random.choice(possible_cells)

                g = Grid(current_grid.row, current_grid.col)
                for x in range(current_grid.row):
                    for y in range(current_grid.col):
                        g.grid[x][y] = copy.deepcopy(current_grid.grid[x][y])

                modify_grid = self.movement.movement(
                    g, selected_cell, target_cell
                )

                new_grid_state = self.grid_to_hash(modify_grid)

                if new_grid_state not in self.visited:
                    self.stack.append(modify_grid)  # إضافة الشبكة الجديدة إلى الكومة
                    print('********************************************')
                    modify_grid.display_grid(modify_grid.grid)

                    if self.movement.isWin(modify_grid):
                        print("Congratulations, you won!")
                        return

        print("No winning configuration found.")
        return None

    def grid_to_hash(self, grid: Grid) -> int:
        return hash(
            tuple(
                tuple((cell.x, cell.y, cell.type) for cell in row)
                for row in grid.grid
            )
        )
