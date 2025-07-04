import heapq
from .search import Problem, Node
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from ui import display_console, display_console_goal

def a_star_search(problem):
    frontier = [(problem.h(problem.initial_state), 0, 0, Node(problem.initial_state))]  # Priority queue: (f_cost, g_cost, unique_id, node)
    visited = {}
    visited[problem.initial_state.to_tuple()] = 0
    unique_id = 1  # To break ties in priority queue
    steps = 0  # Đếm số bước
    
    while frontier:
        f_cost, g_cost, _, node = heapq.heappop(frontier)
        if visited[node.state.to_tuple()] < g_cost:
            continue
        # display_console(node.state)
        steps += 1
        if problem.goal_test(node.state):
            # display_console_goal(node.state)
            print(f"A* đã thực hiện {steps} bước tìm kiếm.")
            return node
        for child in node.expand(problem):
            # Tối ưu: bỏ qua trạng thái cha
            if node.parent and child.state.to_tuple() == node.parent.state.to_tuple():
                continue
            child_tuple = child.state.to_tuple()
            g_cost = child.path_cost  # Cost from start to current node
            h_cost = problem.h(child.state)  # Heuristic cost from current to goal
            f_cost = g_cost + h_cost  # Total estimated cost
            if child_tuple not in visited or g_cost < visited[child_tuple]:
                visited[child_tuple] = g_cost
                heapq.heappush(frontier, (f_cost, g_cost, unique_id, child))
                unique_id += 1
    print(f"A* đã thực hiện {steps} bước tìm kiếm (không tìm thấy lời giải).")
    return None