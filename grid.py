from cell import Cell

class Grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid = [[Cell(x, y, 'E') for y in range(col)] for x in range(row)]
        self.attempts = 3
    def display_grid(self):
        for row in self.grid:
            row_str = ' | '.join(str(cell) for cell in row)
            print(row_str)
            print('-' * len(row_str))

    def input_cell(self, x, y, cell_type):
        if 0 <= x < self.row and 0 <= y < self.col:
            self.grid[x][y] = Cell(x, y, cell_type)

    def choose_cell(self):
        
        user_input = input("Enter 'p' or 'r': ").strip().lower()

        for row in self.grid:
            for cell in row:
                if user_input == 'p' and (cell.type == 'p' or cell.type == 'wp'):
                    return cell
                elif user_input == 'r' and (cell.type == 'r' or cell.type == 'wr'):
                    return cell
        print("No valid cell found for this type.")
        return None

    def movement(self):
        while self.attempts > 0:
            selected_cell = self.choose_cell()
            if selected_cell is None:
                print("Invalid selection. Try again.")
                continue

            try:
                x = int(input("Enter the target x coordinate for movement: "))
                y = int(input("Enter the target y coordinate for movement: "))

                if not (0 <= x < self.row and 0 <= y < self.col):
                    print("Invalid coordinates. Please try again.")
                    continue

                target_cell = self.grid[x][y]

                if target_cell.type in ['E', 'w']:
                    self.attempts -= 1
                    print(f"Attempts remaining: {self.attempts}")

                    if target_cell.type == 'E':
                        self.handle_empty_cell(selected_cell, target_cell)
                    elif target_cell.type == 'w':
                        self.handle_white_cell(selected_cell, target_cell)

                    
                    if target_cell.type in ['p', 'wp']:
                        self.movement_cell_by_purple(target_cell)
                    if target_cell.type in ['r', 'wr']:
                        self.movement_by_red(target_cell)
                    

                    
                    if self.isWin():
                        return
                else:
                    print("Cannot move to that cell. Please choose a different cell.")

            except ValueError:
                print("Invalid input. Please enter integers for coordinates.")

        if self.attempts == 0:
            print("No attempts left. You lost the game.")

    def movement_by_red(self, selected_cell):
        x, y = selected_cell.x, selected_cell.y

        
        if y + 1 < self.col: 
            current_cell = self.grid[x][y + 1]

            if current_cell.type in ['b', 'wb']:
               
                first_b_cell = current_cell 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                return 

       
        for j in range(y + 1, self.col):
            current_cell = self.grid[x][j]

            if current_cell.type in ['b', 'wb']:
                break 

            if current_cell.type == 'w':
               
                first_b_cell = self.grid[x][j - 1] 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                
               
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        if y - 1 >= 0: 
            current_cell = self.grid[x][y - 1]

            if current_cell.type in ['b', 'wb']:
               
                first_b_cell = current_cell 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                return 

       
        for j in range(y - 1, -1, -1):
            current_cell = self.grid[x][j]

            if current_cell.type in ['b', 'wb']:
                break 

            if current_cell.type == 'w':
               
                first_b_cell = self.grid[x][j + 1] 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                
               
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        if x - 1 >= 0: 
            current_cell = self.grid[x - 1][y]

            if current_cell.type in ['b', 'wb']:
               
                first_b_cell = current_cell 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                return 

       
        for i in range(x - 1, -1, -1):
            current_cell = self.grid[i][y]

            if current_cell.type in ['b', 'wb']:
                break 

            if current_cell.type == 'w':
               
                first_b_cell = self.grid[i + 1][y] 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                
               
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        if x + 1 < self.row: 
            current_cell = self.grid[x + 1][y]

            if current_cell.type in ['b', 'wb']:
               
                first_b_cell = current_cell 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                return 

       
        for i in range(x + 1, self.row):
            current_cell = self.grid[i][y]

            if current_cell.type in ['b', 'wb']:
                break 

            if current_cell.type == 'w':
               
                first_b_cell = self.grid[i - 1][y] 
                if first_b_cell.type == 'b':
                    first_b_cell.type = 'E' 
                elif first_b_cell.type == 'wb':
                    first_b_cell.type = 'w' 
                
               
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        self.display_grid()

    def movement_cell_by_purple(self, selected_cell):
        x, y = selected_cell.x, selected_cell.y

       
        found_b = False
        for j in range(y + 1, self.col):
            current_cell = self.grid[x][j]

            if current_cell.type in ['b', 'wb'] and not found_b:
                found_b = True
                first_b_cell = current_cell

            elif found_b and current_cell.type in ['w', 'E']:
                if first_b_cell.type == 'wb':
                    first_b_cell.type = 'w'
                else:
                    first_b_cell.type = 'E'
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        found_b = False
        for j in range(y - 1, -1, -1):
            current_cell = self.grid[x][j]

            if current_cell.type in ['b', 'wb'] and not found_b:
                found_b = True
                first_b_cell = current_cell

            elif found_b and current_cell.type in ['w', 'E']:
                if first_b_cell.type == 'wb':
                    first_b_cell.type = 'w'
                else:
                    first_b_cell.type = 'E'
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        found_b = False
        for i in range(x - 1, -1, -1):
            current_cell = self.grid[i][y]

            if current_cell.type in ['b', 'wb'] and not found_b:
                found_b = True
                first_b_cell = current_cell

            elif found_b and current_cell.type in ['w', 'E']:
                if first_b_cell.type == 'wb':
                    first_b_cell.type = 'w'
                else:
                    first_b_cell.type = 'E'
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        found_b = False
        for i in range(x + 1, self.row):
            current_cell = self.grid[i][y]

            if current_cell.type in ['b', 'wb'] and not found_b:
                found_b = True
                first_b_cell = current_cell

            elif found_b and current_cell.type in ['w', 'E']:
                if first_b_cell.type == 'wb':
                    first_b_cell.type = 'w'
                else:
                    first_b_cell.type = 'E'
                current_cell.type = 'wb' if current_cell.type == 'w' else 'b'
                break

       
        self.display_grid()


    def isWin(self):
        for row in self.grid:
            for cell in row:
                if cell.type == 'w':
                    return False  
        
        print("You won!")
        return True  
   
    def handle_empty_cell(self, selected_cell, target_cell):
     if selected_cell.type == 'wp':
        target_cell.type = 'p'
        self.grid[selected_cell.x][selected_cell.y].type = 'w'
     elif selected_cell.type == 'wr':
        target_cell.type = 'r'
        self.grid[selected_cell.x][selected_cell.y].type = 'w'
     elif selected_cell.type == 'p':
        target_cell.type = 'p'
        self.grid[selected_cell.x][selected_cell.y].type = 'E'
     elif selected_cell.type == 'r':
        target_cell.type = 'r'
        self.grid[selected_cell.x][selected_cell.y].type = 'E'

    def handle_white_cell(self, selected_cell, target_cell):
    
     if selected_cell.type in ['wp', 'wr']:
        self.grid[selected_cell.x][selected_cell.y] = Cell(selected_cell.x, selected_cell.y, 'w')
     elif selected_cell.type in ['p', 'r']:
        self.grid[selected_cell.x][selected_cell.y] = Cell(selected_cell.x, selected_cell.y, 'E')

    
     if selected_cell.type in ['p', 'wp']:
        target_cell.type = 'wp'
     elif selected_cell.type in ['r', 'wr']:
        target_cell.type = 'wr'
    
    
     self.grid[target_cell.x][target_cell.y] = target_cell


    def handle_obstacle_cell(self, selected_cell, target_cell):
     self.grid[selected_cell.x][selected_cell.y].type = 'w' if selected_cell.type in ['wp', 'wr'] else 'E'
     target_cell.type = 'w' 



























     