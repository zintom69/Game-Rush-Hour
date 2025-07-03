from puzzle import *
from ui import *
from algorithms import bfs_search

import time
import sys

pygame.init()
clock = pygame.time.Clock()

# Map game
board = Board()
# print(board.grid)
print(board.stages[0])
board.stagePrepare()
print(board)

display_console(board)

# solution = bfs_search(board)
# for move in solution:
#     display_console(board)
#     pygame.event.pump()
#     time.sleep(0.6)
#     board.move(*move)

# while True:
#     display_console(board)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()