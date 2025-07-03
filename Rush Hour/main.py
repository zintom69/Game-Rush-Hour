from puzzle import *
from ui import *

pygame.init()

board = Board()
# print(board.grid)
print(board.stages[0])
board.stagePrepare()
print(board)

display_console(board)