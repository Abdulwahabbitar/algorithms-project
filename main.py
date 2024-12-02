# main.py

from astar import AStar
from cell import Cell
from dfs import DFS
from grid import Grid
from bfs import BFS
from hc import HC
from movement import Movement
from ucs import UCS


def main():

    g = Grid(5, 5)
    g.input_cell(0, 3, 'w')
    g.input_cell(0, 4, 'w')

    g.input_cell(4, 0, 'w')
    g.input_cell(4, 3, 'w')
    g.input_cell(1, 2, 'b')
    g.input_cell(3, 2, 'b')
    g.input_cell(2, 4, 'p')
    g.input_cell(2, 0, 'r')
    # if you want play:
    
    # g.display_grid(g.grid)
    # m = Movement()
    # while m.isWin(g) == False:
    #     selectedCell = m.choose_cell(g)
    #     if selectedCell==None :
    #         continue
    #     targetCell = m.target_cell(g)
    #     if isinstance(selectedCell, Cell) and isinstance(targetCell, Cell):
    #         m.movement(g, selectedCell, targetCell)
    #         g.display_grid(g.grid)
    #     else:
    #         print("input is wrong")
    g.display_grid(g.grid)
    m = Movement()
    astar= AStar(g)
    astar.search()
    # ucs= UCS(g,Cell(2, 0, 'p'))
    # ucs.search()


main()
# level 5
# g = Grid(4, 3)
# g.input_cell(0, 0, 'w')
# g.input_cell(0, 1, ' ')
# g.input_cell(1, 1, ' ')
# g.input_cell(2, 1, ' ')
# g.input_cell(0, 2, 'w')
# g.input_cell(1, 0, 'wb')
# g.input_cell(1, 2, 'wb')
# g.input_cell(2, 0, 'b')
# g.input_cell(2, 2, 'b')
# g.input_cell(3, 0, 'w')
# g.input_cell(3, 1, 'p')
# g.input_cell(3, 2, 'E')

# level 11
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

#   level 1

# g = Grid(3, 4)
# g.input_cell(1, 1, 'w')

# g.input_cell(1, 3, 'w')

# g.input_cell(1, 2, 'b')

# g.input_cell(2, 0, 'p')

# level 2
# g = Grid(5, 5)
# g.input_cell(0, 2, 'w')
# g.input_cell(2, 0, 'w')

# g.input_cell(2, 2, 'w')
# g.input_cell(2, 4, 'w')
# g.input_cell(4, 2, 'w')
# g.input_cell(1, 2, 'b')
# g.input_cell(2, 1, 'b')
# g.input_cell(2, 3, 'b')
# g.input_cell(3, 2, 'b')
# g.input_cell(4, 0, 'p')

# level 10
# g = Grid(4, 4)
# g.input_cell(1, 1, 'w')
# g.input_cell(1, 3, 'w')

# g.input_cell(3, 0, 'w')
# g.input_cell(3, 3, 'w')
# g.input_cell(2, 2, 'b')
# g.input_cell(2, 3, 'b')
# g.input_cell(3, 1, 'b')
# g.input_cell(0, 0, 'p')

# level 14
# g = Grid(4, 4)
# g.input_cell(1, 0, 'w')
# g.input_cell(1, 2, 'w')

# g.input_cell(2, 1, 'w')
# g.input_cell(2, 2, 'w')
# g.input_cell(0, 3, 'b')
# g.input_cell(2, 0, 'b')
# g.input_cell(3, 0, 'b')
# g.input_cell(3, 3, 'r')

# # level 15
# g = Grid(3, 5)
# g.input_cell(0, 0, 'w')
# g.input_cell(0, 2, 'w')

# g.input_cell(1, 4, 'w')
# g.input_cell(2, 4, 'w')
# g.input_cell(0, 1, 'b')
# g.input_cell(0, 3, 'b')
# g.input_cell(1, 2, 'p')
# g.input_cell(2, 2, 'r')

# level 16
# g = Grid(5, 5)
# g.input_cell(0, 3, 'w')
# g.input_cell(0, 4, 'w')

# g.input_cell(4, 0, 'w')
# g.input_cell(4, 3, 'w')
# g.input_cell(1, 2, 'b')
# g.input_cell(3, 2, 'b')
# g.input_cell(2, 4, 'p')
# g.input_cell(2, 0, 'r')
