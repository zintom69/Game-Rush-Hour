import time
import sys
# import pygame

from puzzle import Board
# from ui import display_console, display_console_goal
from algorithms import Problem, Node, depth_first_tree_search, breadth_first_tree_search, ucs_search, a_star_search


# pygame.init()
# clock = pygame.time.Clock()

# Map game
board = Board()
board.readMap(2)
# print(board.grid)
# print(board.stages[0])
board.stagePrepare()
# print(board)
# display_console(board)

initial_state = board
problem = Problem(initial_state, None)
print(initial_state)

state = initial_state
actions = problem.actions(state)

# state2 = problem.result(state, actions[0])

# for action in actions:
#     tmp_state = problem.result(state, action)
#     print(tmp_state)
# # print(new_state)

# node = Node(initial_state)
# solution = breadth_first_tree_search(problem)
# solution = depth_first_tree_search(problem)
# solution = ucs_search(problem)
solution = a_star_search(problem)


# for i in solution:
#     print(i)

