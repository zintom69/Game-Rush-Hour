import heapq
from .search import Problem, Node
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ui import display_console

def a_star_search(problem):
    frontier = [(problem.h(problem.initial_state) + 0, 0, 0, Node(problem.initial_state))]  # (f_cost, g_cost, unique_id, node)
    visited = {}
    visited[problem.initial_state.to_tuple()] = 0
    unique_id = 1
    # steps = 0
    while frontier:
        f_cost, g_cost, _, node = heapq.heappop(frontier)
        # display_console(node.state)
        if visited[node.state.to_tuple()] < g_cost:
            continue
        # steps += 1
        if problem.goal_test(node.state):
            # print(f"A* đã thực hiện {steps} bước tìm kiếm.")
            # display_console(node.state)
            return node
        for child in node.expand(problem):
            if node.parent and child.state.to_tuple() == node.parent.state.to_tuple():
                continue
            child_tuple = child.state.to_tuple()
            g_cost = child.path_cost  # path_cost now includes vehicle length
            h_cost = problem.h(child.state)
            f_cost = g_cost + h_cost
            if child_tuple not in visited or g_cost < visited[child_tuple]:
                visited[child_tuple] = g_cost
                heapq.heappush(frontier, (f_cost, g_cost, unique_id, child))
                unique_id += 1
    # print(f"A* đã thực hiện {steps} bước tìm kiếm (không tìm thấy lời giải).")
    return None