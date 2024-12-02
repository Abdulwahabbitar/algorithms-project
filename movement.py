import copy
from cell import Cell
from grid import Grid
from typing import List


class Movement:
    def __init__(self):

        self.attempts = 3

    def choose_cell(self, grid: Grid) -> Cell:

        user_input = input("Enter 'p' or 'r': ").strip().lower()

        for row in grid.grid:
            for cell in row:
                if user_input == 'p' and (cell.type == 'p' or cell.type == 'wp'):
                    return cell
                elif user_input == 'r' and (cell.type == 'r' or cell.type == 'wr'):
                    return cell
        print("No valid cell found for this type.")
        return None

    def target_cell(self, grid: Grid) -> Cell:
        print("Enter the target cell")
        x = int(input("Enter X : "))
        y = int(input("Enter y : "))

        if 0 <= x < grid.row and 0 <= y < grid.col:
            for row in grid.grid:
                for cell in row:
                    if cell.x == x and cell.y == y and cell.type in ['E', 'w']:
                        return cell
        else:
            return None

    def movement(self, grid: Grid, selected_cell, target_cell) -> Grid:

        if target_cell.type == 'E':
            self.handle_empty_cell(selected_cell, target_cell, grid)

        elif target_cell.type == 'w':
            self.handle_white_cell(selected_cell, target_cell, grid)

        if grid.grid[target_cell.x][target_cell.y].type in ['p', 'wp']:
            self.movement_cell_by_purple(
                grid.grid[target_cell.x][target_cell.y], grid)
        if grid.grid[target_cell.x][target_cell.y].type in ['r', 'wr']:
            self.movement_by_red(grid.grid[target_cell.x][target_cell.y], grid)

        return grid

    def isWin(self, grid: Grid):
        for row in grid.grid:
            for cell in row:
                if cell.type == 'w':
                    return False

        print("You won!")
        return True

    def handle_empty_cell(self, selected_cell: Cell, target_cell: Cell, grid: Grid):
        if selected_cell.type == 'wp':
            grid.grid[target_cell.x][target_cell.y].type = 'p'
            grid.grid[selected_cell.x][selected_cell.y].type = 'w'
        elif selected_cell.type == 'wr':
            grid.grid[target_cell.x][target_cell.y].type = 'r'
            grid.grid[selected_cell.x][selected_cell.y].type = 'w'
        elif selected_cell.type == 'p':

            grid.grid[selected_cell.x][selected_cell.y].type = 'E'
            grid.grid[target_cell.x][target_cell.y].type = 'p'
        elif selected_cell.type == 'r':
            grid.grid[target_cell.x][target_cell.y].type = 'r'
            grid.grid[selected_cell.x][selected_cell.y].type = 'E'

    def handle_white_cell(self, selected_cell, target_cell, grid: Grid):

        if selected_cell.type == 'wp':
            grid.grid[target_cell.x][target_cell.y].type = 'wp'
            grid.grid[selected_cell.x][selected_cell.y].type = 'w'
        elif selected_cell.type == 'wr':
            grid.grid[target_cell.x][target_cell.y].type = 'wr'
            grid.grid[selected_cell.x][selected_cell.y].type = 'w'
        elif selected_cell.type == 'p':

            grid.grid[selected_cell.x][selected_cell.y].type = 'E'
            grid.grid[target_cell.x][target_cell.y].type = 'wp'
        elif selected_cell.type == 'r':
            grid.grid[target_cell.x][target_cell.y].type = 'wr'
            grid.grid[selected_cell.x][selected_cell.y].type = 'E'

    def move_cell(self, current_cell, next_cell):
        if current_cell.type == 'b':
            current_cell.type = 'E'
            next_cell.type = 'b' if next_cell.type == 'E' else 'wb' if next_cell.type == 'w' else next_cell.type
        elif current_cell.type == 'wb':
            current_cell.type = 'w'
            next_cell.type = 'b' if next_cell.type == 'E' else 'wb' if next_cell.type == 'w' else next_cell.type
        elif current_cell.type == 'r':
            current_cell.type = 'E'
            next_cell.type = 'r' if next_cell.type == 'E' else 'wr' if next_cell.type == 'w' else next_cell.type
        elif current_cell.type == 'wr':
            current_cell.type = 'w'
            next_cell.type = 'r' if next_cell.type == 'E' else 'wr' if next_cell.type == 'w' else next_cell.type

    def movement_cell_by_purple(self, selected_cell, grid: Grid):
        x, y = selected_cell.x, selected_cell.y

        def is_edge(x, y, direction):
            if direction == 'up':
                return x == 0
            elif direction == 'down':
                return x == grid.row - 1
            elif direction == 'right':
                return y == grid.col - 1
            elif direction == 'left':
                return y == 0
            return False

        def process_direction(dx, dy, direction):
            stack = []
            found_movable_cell = False
            i, j = x + dx, y + dy

            while 0 <= i < grid.row and 0 <= j < grid.col:
                current_cell = grid.grid[i][j]
                if current_cell.type in ['b', 'wb', 'r', 'wr']:
                    stack.append(current_cell)
                    found_movable_cell = True
                    i += dx
                    j += dy
                    continue
                elif current_cell.type in ['w', 'E'] and found_movable_cell:
                    break
                i += dx
                j += dy

            if stack:
                while stack:
                    current_cell = stack.pop()
                    if not is_edge(current_cell.x, current_cell.y, direction):
                        next_cell = grid.grid[current_cell.x +
                                              dx][current_cell.y + dy]
                        if next_cell.type in ['w', 'E']:
                            self.move_cell(current_cell, next_cell)

        process_direction(-1, 0, 'up')
        process_direction(1, 0, 'down')
        process_direction(0, 1, 'right')
        process_direction(0, -1, 'left')

    def movement_by_red(self, selected_cell, grid: Grid):
        x, y = selected_cell.x, selected_cell.y

        directions = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]

        for dx, dy in directions:
            i, j = x + dx, y + dy
            if 0 <= i < grid.row and 0 <= j < grid.col and grid.grid[i][j].type not in ['b', 'wb']:
                switched_b = False
                while 0 <= i < grid.row and 0 <= j < grid.col:
                    current_cell = grid.grid[i][j]
                    first_b_cell = grid.grid[i - dx][j - dy] if 0 <= i - \
                        dx < grid.row and 0 <= j - dy < grid.col else None
                    before_first_b_cell = grid.grid[i - 2 * dx][j - 2 * dy] if 0 <= i - \
                        2 * dx < grid.row and 0 <= j - 2 * dy < grid.col else None

                    if first_b_cell and before_first_b_cell:
                        switched_b = self.move_and_switch(
                            current_cell, first_b_cell, before_first_b_cell, switched_b)

                    i += dx
                    j += dy

    def get_possible_moves(self, grid: Grid) -> List[Cell]:
        possible_moves: List[Cell] = []
        for row in grid.grid:
            for cell in row:
                if cell.type in ['w', 'E']:

                    possible_moves.append(cell)
        return possible_moves

    def move_and_switch(self, current_cell, first_b_cell, before_first_b_cell, switched_b):

        if current_cell.type == 'b' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or not switched_b):
            current_cell.type = 'E'
            if first_b_cell.type == 'E':
                first_b_cell.type = 'b'
            elif first_b_cell.type == 'w':
                first_b_cell.type = 'wb'
            return True
        elif current_cell.type == 'wb' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
            current_cell.type = 'w'
            if first_b_cell.type == 'E':
                first_b_cell.type = 'b'
            elif first_b_cell.type == 'w':
                first_b_cell.type = 'wb'
        elif current_cell.type == 'p' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or not switched_b):
            current_cell.type = 'E'
            if first_b_cell.type == 'E':
                first_b_cell.type = 'p'
            elif first_b_cell.type == 'w':
                first_b_cell.type = 'wp'
            return True
        elif current_cell.type == 'wp' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
            current_cell.type = 'w'
            if first_b_cell.type == 'E':
                first_b_cell.type = 'p'
            elif first_b_cell.type == 'w':
                first_b_cell.type = 'wp'
        return switched_b

    def get_heuristic(self, grid: Grid) -> float:
        heuristic_value = 0

        magnetic_cells = []
        white_cells = []

        for row in grid.grid:
            for cell in row:
                if cell.type in ['p', 'r', 'b', 'wp', 'wr']:
                    magnetic_cells.append(cell)
                elif cell.type == 'w':
                    white_cells.append(cell)

        for mag_cell in magnetic_cells:
            total_distance = 0
            for white_cell in white_cells:

                distance = abs(mag_cell.x - white_cell.x) + \
                    abs(mag_cell.y - white_cell.y)

                total_distance += distance

            heuristic_value += total_distance

        for i, mag_cell1 in enumerate(magnetic_cells):
            for j, mag_cell2 in enumerate(magnetic_cells):
                if i < j:
                    distance = abs(mag_cell1.x - mag_cell2.x) + \
                        abs(mag_cell1.y - mag_cell2.y)
                    if distance < 2:
                        heuristic_value += 5

        return heuristic_value
