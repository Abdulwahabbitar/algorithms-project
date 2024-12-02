class Cell:
    def __init__(self, x, y, cell_type='E',):
        self.x = x
        self.y = y
        self.type = cell_type
   
    def __str__(self):
            return f"{self.type}"
    def __deepcopy__(self, memo):
        new_cell = Cell(self.x, self.y, self.type)
        return new_cell