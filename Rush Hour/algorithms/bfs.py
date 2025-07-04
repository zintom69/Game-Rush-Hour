from collections import deque
from .search import Problem, Node
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ui import display_console, display_console_goal

def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial_state)])  # FIFO queue
    visited = set()
    visited.add(problem.initial_state.to_tuple())

    while frontier:
        node = frontier.popleft()
        display_console(node.state)
        if problem.goal_test(node.state):
            display_console_goal(node.state) 
            return node
        for child in node.expand(problem):
            child_tuple = child.state.to_tuple()
            if child_tuple not in visited:
                visited.add(child_tuple)
                frontier.append(child)
    return None