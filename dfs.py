import copy
from cell import Cell
from grid import Grid
from movement import Movement


class DFS:
    def __init__(self, grid: Grid, selected_cell: Cell):
        self.grid = grid
        self.movement = Movement()
        self.selected_cell = selected_cell
        self.stack = [(selected_cell, self.grid)]
        self.visited = set()
        self.visited.add((selected_cell, self.grid))
   
    def search(self):
        while self.stack:
            current_position, current_grid = self.stack.pop()  # نستخدم pop من النهاية لتحقيق البحث بالعمق أولاً

            # تحقق مما إذا كنا في الحالة الفائزة
            if self.movement.isWin(current_grid):
                print("Congratulations, you won!")
                return current_grid

            # استكشاف الحركات الممكنة من الموقع الحالي
            possible_moves = self.movement.get_possible_moves(current_grid)
            
            for target_cell in possible_moves:
                # إنشاء نسخة عميقة من current_grid لحفظ الحالة الأصلية
                copy_from_current_grid = copy.deepcopy(current_grid)

                # تمرير نسخة عميقة لتابع movement وتحديث الشبكة المعدلة
                modified_grid = self.movement.movement(copy_from_current_grid, current_position, target_cell)
                
                print("Modified current Grid after movement:")
                modified_grid.display_grid()  # تحقق من الشبكة بعد الحركة
                
                # إضافة الشبكة المعدلة إلى المكدس مع الموقع الجديد
                if (target_cell.x, target_cell.y) not in self.visited:
                    self.visited.add((target_cell.x, target_cell.y))
                    self.stack.append((target_cell, modified_grid))
                    
        print("No winning configuration found.")
        return None
