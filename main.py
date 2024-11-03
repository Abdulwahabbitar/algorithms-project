# main.py

from grid import Grid

def main():
    g = Grid(4, 3)
    g.input_cell(0, 0, 'w')
    g.input_cell(0, 1, ' ')
    g.input_cell(1, 1, ' ')
    g.input_cell(2, 1, ' ')
    g.input_cell(0, 2, 'w')
    g.input_cell(1, 0, 'wb')
    g.input_cell(1, 2, 'wb')
    g.input_cell(2, 0, 'b')
    g.input_cell(2, 2, 'b')
    g.input_cell(3, 0, 'w')
    g.input_cell(3, 1, 'p') 
    g.input_cell(3, 2, 'E')
    # g = Grid(2, 5)
    # g.input_cell(0, 0, 'b')
    # g.input_cell(0, 1, 'w')
  
    # g.input_cell(0, 2, 'w')
    # g.input_cell(0, 3, 'w')
    # g.input_cell(0, 4, 'b')
   
    # g.input_cell(1, 0, ' ')
    # g.input_cell(1, 1, ' ')
    # g.input_cell(1, 2, 'r')
    # g.input_cell(1, 3, ' ')
    # g.input_cell(1, 4, ' ')
  

    g.display_grid()
  
    g.movement() 

    
            
        
            

main()
