from collections import deque
from .search import Problem, Node
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from ui import display_console, display_console_goal

def depth_first_tree_search(problem):
    frontier = [Node(problem.initial_state)]  # LIFO stack (list)
    visited = set()
    visited.add(problem.initial_state.to_tuple())
    steps = 0  # Đếm số bước
    
    while frontier:
        node = frontier.pop()  # Pop from end (LIFO)
        # display_console(node.state)
        steps += 1
        if problem.goal_test(node.state):
            # display_console_goal(node.state)
            print(f"DFS đã thực hiện {steps} bước tìm kiếm.")
            return node
        for child in node.expand(problem):
            child_tuple = child.state.to_tuple()
            if child_tuple not in visited:
                visited.add(child_tuple)
                frontier.append(child)
    print(f"DFS đã thực hiện {steps} bước tìm kiếm (không tìm thấy lời giải).")
    return None