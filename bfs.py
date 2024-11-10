import copy
from cell import Cell
from grid import Grid
from movement import Movement


class BFS:
    def __init__(self, grid: Grid, selected_cell:Cell):
        self.grid = grid
        self.movement= Movement()
        self.selected_cell = selected_cell
        self.queue = [(selected_cell, self.grid)]
        self.visited = set()
        self.visited.add((selected_cell, self.grid))
   
    def search(self):
        while self.queue:
            current_position, current_grid = self.queue.pop(0)

            # تحقق مما إذا كنا في الحالة الفائزة
            if self.movement.isWin(current_grid):
                print("Congratulations, you won!")
                return current_grid

            # استكشاف الحركات الممكنة من الموقع الحالي
            possible_moves = self.movement.get_possible_moves(current_grid)

            for target_cell in possible_moves:
                # إنشاء نسخة جديدة من الشبكة باستخدام الحركة
                modified_grid = self.movement.movement(current_grid, current_position, target_cell)

                print("Modified current Grid after movement:")
                modified_grid.display_grid()

                # إضافة الشبكة المعدلة إلى الطابور مع الموقع الجديد إذا لم يتم زيارتها
                if (target_cell.x, target_cell.y) not in self.visited:
                    self.visited.add((target_cell.x, target_cell.y))
                    self.queue.append((target_cell, modified_grid))
                    
        print("No winning configuration found.")
        return None
