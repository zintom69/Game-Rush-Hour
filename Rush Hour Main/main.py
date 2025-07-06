import time
import sys
# import psutil
import csv
import os
import tracemalloc
from collections import deque
# import pygame

from puzzle import Board
from ui import display_console
from algorithms import Problem, Node, depth_first_tree_search, breadth_first_tree_search, ucs_search, a_star_search


# pygame.init()
# clock = pygame.time.Clock()

# Map game
board = Board()
board.readMap(0)
# print(board.grid)
# print(board.stages[0])
board.stagePrepare()
# print(board)
display_console(board)

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
# solution = a_star_search(problem)

# def measure_search(algorithm_name, search_func, problem):
#     process = psutil.Process(os.getpid())
#     tracemalloc.start()
#     start_time = time.time()
#     mem_before = process.memory_info().rss
#     expanded_nodes = [0]
    
#     def wrapper(*args, **kwargs):
#         result = None
#         if algorithm_name == 'bfs':
#             def bfs_count(problem):
#                 frontier = deque([Node(problem.initial_state)])
#                 visited = set()
#                 visited.add(problem.initial_state.to_tuple())
#                 steps = 0
#                 while frontier:
#                     node = frontier.popleft()
#                     steps += 1
#                     if problem.goal_test(node.state):
#                         expanded_nodes[0] = steps
#                         return node
#                     for child in node.expand(problem):
#                         child_tuple = child.state.to_tuple()
#                         if child_tuple not in visited:
#                             visited.add(child_tuple)
#                             frontier.append(child)
#                 expanded_nodes[0] = steps
#                 return None
#             result = bfs_count(problem)
#         elif algorithm_name == 'dfs':
#             def dfs_count(problem):
#                 frontier = [Node(problem.initial_state)]
#                 visited = set()
#                 visited.add(problem.initial_state.to_tuple())
#                 steps = 0
#                 while frontier:
#                     node = frontier.pop()
#                     steps += 1
#                     if problem.goal_test(node.state):
#                         expanded_nodes[0] = steps
#                         return node
#                     for child in node.expand(problem):
#                         child_tuple = child.state.to_tuple()
#                         if child_tuple not in visited:
#                             visited.add(child_tuple)
#                             frontier.append(child)
#                 expanded_nodes[0] = steps
#                 return None
#             result = dfs_count(problem)
#         elif algorithm_name == 'ucs':
#             def ucs_count(problem):
#                 steps = 0
#                 def patch_expand(self, problem):
#                     nonlocal steps
#                     steps += 1
#                     return [self.child_node(problem, action) for action in problem.actions(self.state)]
#                 orig_expand = Node.expand
#                 Node.expand = patch_expand
#                 try:
#                     res = ucs_search(problem)
#                 finally:
#                     Node.expand = orig_expand
#                 expanded_nodes[0] = steps
#                 return res
#             result = ucs_count(problem)
#         elif algorithm_name == 'a_star':
#             def a_star_count(problem):
#                 steps = 0
#                 def patch_expand(self, problem):
#                     nonlocal steps
#                     steps += 1
#                     return [self.child_node(problem, action) for action in problem.actions(self.state)]
#                 orig_expand = Node.expand
#                 Node.expand = patch_expand
#                 try:
#                     res = a_star_search(problem)
#                 finally:
#                     Node.expand = orig_expand
#                 expanded_nodes[0] = steps
#                 return res
#             result = a_star_count(problem)
#         else:
#             # fallback for other algorithms
#             def search_count(problem, search_func):
#                 steps = 0
#                 def patch_expand(self, problem):
#                     nonlocal steps
#                     steps += 1
#                     return [self.child_node(problem, action) for action in problem.actions(self.state)]
#                 orig_expand = Node.expand
#                 Node.expand = patch_expand
#                 try:
#                     res = search_func(problem)
#                 finally:
#                     Node.expand = orig_expand
#                 expanded_nodes[0] = steps
#                 return res
#             result = search_count(problem, search_func)
#         return result
#     wrapper(problem)
#     mem_after = process.memory_info().rss
#     end_time = time.time()
#     current, peak = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#     search_time = end_time - start_time
#     memory_usage = max(mem_after, peak) / (1024 * 1024)  # MB
#     return search_time, memory_usage, expanded_nodes[0]

# def write_metrics(algorithm, search_time, memory_usage, expanded_nodes):
#     with open('map0.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([algorithm, f'{search_time:.6f}', f'{memory_usage:.2f}', expanded_nodes])

# if __name__ == "__main__":
#     # ...existing code...
#     algos = [
#         ("bfs", breadth_first_tree_search),
#         ("dfs", depth_first_tree_search),
#         ("ucs", ucs_search),
#         ("a_star", a_star_search)
#     ]
#     for name, func in algos:
#         search_time, memory_usage, expanded_nodes = measure_search(name, func, problem)
#         write_metrics(name, search_time, memory_usage, expanded_nodes)
#         print(f"{name}: time={search_time:.4f}s, mem={memory_usage:.2f}MB, expanded={expanded_nodes}")