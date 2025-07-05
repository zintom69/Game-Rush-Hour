import heapq
from .search import Problem, Node
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from ui import display_console, display_console_goal

def ucs_search(problem):
    frontier = [(0, 0, Node(problem.initial_state))]  # Priority queue: (cost, unique_id, node)
    visited = {}
    visited[problem.initial_state.to_tuple()] = 0
    unique_id = 1  # To break ties in priority queue
    # steps = 0  # Đếm số bước
    
    while frontier:
        cost, _, node = heapq.heappop(frontier)
        if visited[node.state.to_tuple()] < cost:
            continue
        # display_console(node.state)
        # steps += 1
        if problem.goal_test(node.state):
            # display_console_goal(node.state)
            # print(f"UCS đã thực hiện {steps} bước tìm kiếm.")
            return node
        for child in node.expand(problem):
            if node.parent and child.state.to_tuple() == node.parent.state.to_tuple():
                continue
            child_tuple = child.state.to_tuple()
            if child_tuple not in visited or child.path_cost < visited[child_tuple]:
                visited[child_tuple] = child.path_cost
                heapq.heappush(frontier, (child.path_cost, unique_id, child))
                unique_id += 1
    # print(f"UCS đã thực hiện {steps} bước tìm kiếm (không tìm thấy lời giải).")
    return None