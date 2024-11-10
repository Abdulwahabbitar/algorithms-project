import copy
from cell import Cell


class Grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid = [[Cell(x, y, 'E') for y in range(col)] for x in range(row)]
        self.attempts = 3
    def __deepcopy__(self, memo):
        # إنشاء نسخة جديدة من Grid مع نسخ جميع الخلايا بشكل عميق
        new_grid = Grid(self.row, self.col)
        new_grid.grid = [[copy.deepcopy(cell) for cell in row] for row in self.grid]
        return new_grid
    def display_grid(self):
        for row in self.grid:
            row_str = ' | '.join(str(cell) for cell in row)
            print(row_str)
            print('-' * len(row_str))

    def input_cell(self, x, y, cell_type):
        if 0 <= x < self.row and 0 <= y < self.col:
            self.grid[x][y] = Cell(x, y, cell_type)

    # def choose_cell(self):

    #     user_input = input("Enter 'p' or 'r': ").strip().lower()

    #     for row in self.grid:
    #         for cell in row:
    #             if user_input == 'p' and (cell.type == 'p' or cell.type == 'wp'):
    #                 return cell
    #             elif user_input == 'r' and (cell.type == 'r' or cell.type == 'wr'):
    #                 return cell
    #     print("No valid cell found for this type.")
    #     return None

    # def movement(self):
    #     while self.attempts > 0:
    #         selected_cell = self.choose_cell()
    #         if selected_cell is None:
    #             print("Invalid selection. Try again.")
    #             continue

    #         try:
    #             x = int(input("Enter the target x coordinate for movement: "))
    #             y = int(input("Enter the target y coordinate for movement: "))

    #             if not (0 <= x < self.row and 0 <= y < self.col):
    #                 print("Invalid coordinates. Please try again.")
    #                 continue

    #             target_cell = self.grid[x][y]

    #             if target_cell.type in ['E', 'w']:
    #                 self.attempts -= 1
    #                 print(f"Attempts remaining: {self.attempts}")

    #                 if target_cell.type == 'E':
    #                     self.handle_empty_cell(selected_cell, target_cell)
    #                 elif target_cell.type == 'w':
    #                     self.handle_white_cell(selected_cell, target_cell)

    #                 if target_cell.type in ['p', 'wp']:
    #                     self.movement_cell_by_purple(target_cell)
    #                 if target_cell.type in ['r', 'wr']:
    #                     self.movement_by_red(target_cell)

    #                 if self.isWin():
    #                     return
    #             else:
    #                 print("Cannot move to that cell. Please choose a different cell.")

    #         except ValueError:
    #             print("Invalid input. Please enter integers for coordinates.")

    #     if self.attempts == 0:
    #         print("No attempts left. You lost the game.")

    # def movement_by_red(self, selected_cell):
    #     x, y = selected_cell.x, selected_cell.y

    #     if y+1 < self.col:
    #         if self.grid[x][y+1].type not in ['b', 'wb']:
    #             for j in range(y + 1, self.col):

    #                 current_cell = self.grid[x][j]
    #                 if j-1 >= 0:
    #                     first_b_cell = self.grid[x][j - 1]
    #                 if j-2 >= 0:
    #                     before_first_b_cell = self.grid[x][j - 2]
    #                 switched_b = False
    #                 if current_cell.type == 'b' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):
    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'

    #                 if current_cell.type == 'wb' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'
    #                 if current_cell.type == 'p' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):
    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'p'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wp'

    #                 if current_cell.type == 'wp' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'p'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wp'
    #     if y-1 >= 0:
    #         if self.grid[x][y - 1].type not in ['b', 'wb']:
    #             for j in range(y - 1, -1, -1):

    #                 current_cell = self.grid[x][j]
    #                 if j+1 < self.col:
    #                     first_b_cell = self.grid[x][j + 1]
    #                 if j+2 < self.col:
    #                     before_first_b_cell = self.grid[x][j + 2]
    #                 switched_b = False
    #                 if current_cell.type == 'b' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):
    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'

    #                 if current_cell.type == 'wb' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'
    #     if x-1 >= 0:
    #         if self.grid[x-1][y].type not in ['b', 'wb']:
    #             for i in range(x - 1, -1, -1):

    #                 current_cell = self.grid[i][y]
    #                 if i+1 < self.row:
    #                     first_b_cell = self.grid[i + 1][y]
    #                 if i+2 < self.row:
    #                     before_first_b_cell = self.grid[i + 2][y]
    #                 switched_b = False
    #                 if current_cell.type == 'b' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):
    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'

    #                 if current_cell.type == 'wb' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'
    #                 if current_cell.type == 'p' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):
    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'p'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wp'

    #                 if current_cell.type == 'wp' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'p'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wp'

    #     if x+1 < self.row:
    #         if self.grid[x+1][y].type not in ['b', 'wb']:
    #             for i in range(x + 1, self.row):

    #                 current_cell = self.grid[i][y]
    #                 if i-1 >= 0:
    #                     first_b_cell = self.grid[i - 1][y]
    #                 if i-2 >= 0:
    #                     before_first_b_cell = self.grid[i - 2][y]

    #                 switched_b = False
    #                 if current_cell.type == 'b' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):

    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'

    #                 if current_cell.type == 'wb' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'b'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wb'

    #                 if current_cell.type == 'p' and first_b_cell.type in ['E', 'w'] and (before_first_b_cell.type not in ['E', 'w'] or switched_b == False):
    #                     current_cell.type = 'E'
    #                     switched_b = True
    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'p'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wp'

    #                 if current_cell.type == 'wp' and first_b_cell.type in ['E', 'w'] and before_first_b_cell.type not in ['E', 'w']:
    #                     current_cell.type = 'w'

    #                     if first_b_cell.type == 'E':
    #                         first_b_cell.type = 'p'
    #                     elif first_b_cell.type == 'w':
    #                         first_b_cell.type = 'wp'
    #     self.display_grid()

   
    # def movement_cell_by_purple(self, selected_cell):
    #     x, y = selected_cell.x, selected_cell.y
    #     print('YES')

    #     # التحقق من كون الخلية على الحافة
    #     def is_edge_up(x, y):
    #         return x == 0  # حافة الشبكة في الاتجاه الأعلى

    #     def is_edge_down(x, y):
    #         return x == self.row - 1  # حافة الشبكة في الاتجاه الأسفل

    #     def is_edge_right(x, y):
    #         return y == self.col - 1  # حافة الشبكة في الاتجاه اليمين

    #     def is_edge_left(x, y):
    #         return y == 0  # حافة الشبكة في الاتجاه اليسار

    #     # الاتجاه: الأعلى
    #     stack_up = []
    #     found_movable_cell_up = False
    #     for i in range(x - 1, -1, -1):  # الحركة للأعلى
    #         current_cell = self.grid[i][y]

    #         # إضافة الخلايا القابلة للتحرك إلى الستاك
    #         if current_cell.type in ['b', 'wb', 'r', 'wr']:
    #             stack_up.append(current_cell)
    #             found_movable_cell_up = True
    #             continue
    #         elif current_cell.type in ['w', 'E'] and found_movable_cell_up:
    #             break

    #     if stack_up:
    #         while stack_up:
    #             current_cell = stack_up.pop()
    #             if not is_edge_up(current_cell.x, current_cell.y):  # التحقق من الحافة للأعلى
    #                 next_cell = self.grid[current_cell.x - 1][current_cell.y]
    #                 if next_cell.type in ['w', 'E']:
    #                     self.move_cell(current_cell, next_cell)

    #     # الاتجاه: الأسفل
    #     stack_down = []
    #     found_movable_cell_down = False
    #     for i in range(x + 1, self.row):  # الحركة للأسفل
    #         current_cell = self.grid[i][y]

    #         if current_cell.type in ['b', 'wb', 'r', 'wr']:
    #             stack_down.append(current_cell)
    #             found_movable_cell_down = True
    #             continue
    #         elif current_cell.type in ['w', 'E'] and found_movable_cell_down:
    #             break

    #     if stack_down:
    #         while stack_down:
    #             current_cell = stack_down.pop()
    #             if not is_edge_down(current_cell.x, current_cell.y):  # التحقق من الحافة للأسفل
    #                 next_cell = self.grid[current_cell.x + 1][current_cell.y]
    #                 if next_cell.type in ['w', 'E']:
    #                     self.move_cell(current_cell, next_cell)

    #     # الاتجاه: اليمين
    #     stack_right = []
    #     found_movable_cell_right = False
    #     for i in range(y + 1, self.col):  # الحركة لليمين
    #         current_cell = self.grid[x][i]

    #         # التأكد من أن الخلية قابلة للتحرك مع التحقق من الحافة في الاتجاه اليمين فقط
    #         if current_cell.type in ['b', 'wb', 'r', 'wr'] and not is_edge_right(x, i):
    #             stack_right.append(current_cell)
    #             found_movable_cell_right = True
    #             continue
    #         elif current_cell.type in ['w', 'E'] and found_movable_cell_right:
    #             break

    #     if stack_right:
    #         while stack_right:
    #             current_cell = stack_right.pop()
    #             if not is_edge_right(current_cell.x, current_cell.y):  # التحقق من الحافة في الاتجاه اليمين
    #                 next_cell = self.grid[current_cell.x][current_cell.y + 1]
    #                 if next_cell.type in ['w', 'E']:
    #                     self.move_cell(current_cell, next_cell)

    #     # الاتجاه: اليسار
    #     stack_left = []
    #     found_movable_cell_left = False
    #     for i in range(y - 1, -1, -1):  # الحركة لليسار
    #         current_cell = self.grid[x][i]

    #         # إضافة الخلايا القابلة للتحرك إلى الستاك
    #         if current_cell.type in ['b', 'wb', 'r', 'wr']:
    #             stack_left.append(current_cell)
    #             found_movable_cell_left = True
    #             continue
    #         elif current_cell.type in ['w', 'E'] and found_movable_cell_left:
    #             break

    #     if stack_left:
    #         while stack_left:
    #             current_cell = stack_left.pop()
    #             if not is_edge_left(current_cell.x, current_cell.y):  # التحقق من الحافة لليسار
    #                 next_cell = self.grid[current_cell.x][current_cell.y - 1]
    #                 if next_cell.type in ['w', 'E']:
    #                     self.move_cell(current_cell, next_cell)

    #     # استدعاء عرض الشبكة بعد الحركة
    #     self.display_grid()

    # def move_cell(self, current_cell, next_cell):
    #     # منطق تحريك الخلايا
    #     if current_cell.type == 'b':
    #         current_cell.type = 'E'
    #         next_cell.type = 'b' if next_cell.type == 'E' else 'wb' if next_cell.type == 'w' else next_cell.type
    #     elif current_cell.type == 'wb':
    #         current_cell.type = 'w'
    #         next_cell.type = 'b' if next_cell.type == 'E' else 'wb' if next_cell.type == 'w' else next_cell.type
    #     elif current_cell.type == 'r':
    #         current_cell.type = 'E'
    #         next_cell.type = 'r' if next_cell.type == 'E' else 'wr' if next_cell.type == 'w' else next_cell.type
    #     elif current_cell.type == 'wr':
    #         current_cell.type = 'w'
    #         next_cell.type = 'r' if next_cell.type == 'E' else 'wr' if next_cell.type == 'w' else next_cell.type

    # def isWin(self):
    #     for row in self.grid:
    #         for cell in row:
    #             if cell.type == 'w':
    #                 return False

    #     print("You won!")
    #     return True

    # def handle_empty_cell(self, selected_cell, target_cell):
    #     if selected_cell.type == 'wp':
    #         target_cell.type = 'p'
    #         self.grid[selected_cell.x][selected_cell.y].type = 'w'
    #     elif selected_cell.type == 'wr':
    #         target_cell.type = 'r'
    #         self.grid[selected_cell.x][selected_cell.y].type = 'w'
    #     elif selected_cell.type == 'p':
    #         target_cell.type = 'p'
    #         self.grid[selected_cell.x][selected_cell.y].type = 'E'
    #     elif selected_cell.type == 'r':
    #         target_cell.type = 'r'
    #         self.grid[selected_cell.x][selected_cell.y].type = 'E'

    # def handle_white_cell(self, selected_cell, target_cell):

    #     if selected_cell.type in ['wp', 'wr']:
    #         self.grid[selected_cell.x][selected_cell.y] = Cell(
    #             selected_cell.x, selected_cell.y, 'w')
    #     elif selected_cell.type in ['p', 'r']:
    #         self.grid[selected_cell.x][selected_cell.y] = Cell(
    #             selected_cell.x, selected_cell.y, 'E')

    #     if selected_cell.type in ['p', 'wp']:
    #         target_cell.type = 'wp'
    #     elif selected_cell.type in ['r', 'wr']:
    #         target_cell.type = 'wr'

    #     self.grid[target_cell.x][target_cell.y] = target_cell

    # def handle_obstacle_cell(self, selected_cell, target_cell):
    #     self.grid[selected_cell.x][selected_cell.y].type = 'w' if selected_cell.type in [
    #         'wp', 'wr'] else 'E'
    #     target_cell.type = 'w'
