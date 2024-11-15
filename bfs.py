import copy
from cell import Cell
from grid import Grid
from movement import Movement

class BFS:
    def __init__(self, grid: Grid, selected_cell: Cell):
        self.grid = grid
        self.movement = Movement()
        self.selected_cell = selected_cell
        self.queue = [(selected_cell, self.grid)]
        self.visited = set()
        self.visited.add(self.grid_to_string(grid))  # إضافة حالة الشبكة الأولى

    def search(self):
        while self.queue:
            current_position, current_grid = self.queue.pop(0)

            

            possible_moves = self.movement.get_possible_moves(current_grid)
            new_grid_generated = False  # متغير لتتبع ما إذا تم توليد شبكات جديدة

            for target_cell in possible_moves:
                
                # نسخ الشبكة الحالية
                copy_of_grid = copy.deepcopy(current_grid)

                # تنفيذ الحركة
                modify_grid = self.movement.movement(
                    copy_of_grid, current_position, target_cell)
                
                # تمثيل الشبكة الجديدة
                grid_state = self.grid_to_string(modify_grid)

                # تحقق مما إذا كانت الشبكة الجديدة قد زارت من قبل
                if grid_state not in self.visited:
                    self.visited.add(grid_state)  # أضفها إلى المزارات
                    modify_grid.display_grid()
                    if self.movement.isWin(modify_grid):
                      print("Congratulations, you won!")
                      return
                    self.queue.append((target_cell, modify_grid))
                    new_grid_generated = True  # تم توليد شبكة جديدة

            # بعد أن تم توليد الحركات الممكنة، قم بإضافة الشبكة الحالية إلى الزيارة
            if new_grid_generated:
                self.visited.add(self.grid_to_string(current_grid))
            
        print("No winning configuration found.")
        return None

    def grid_to_string(self, grid: Grid) -> str:
        # تحويل الشبكة إلى سلسلة فريدة لتتبع الزيارات
        return ''.join([cell.type for row in grid.grid for cell in row])
