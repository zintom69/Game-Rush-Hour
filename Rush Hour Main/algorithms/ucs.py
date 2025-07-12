import heapq
from .search import Problem, Node, time, TIME_LIMIT

def ucs_search(problem):
    frontier = [(0, 0, Node(problem.initial_state))]  # Priority queue: (cost, unique_id, node)
    visited = {}
    visited[problem.initial_state.to_tuple()] = 0
    unique_id = 1 
    start_time = time.time()
    
    while frontier:
        if time.time() - start_time > TIME_LIMIT:
            print("Time limit exceeded!")
            return None
        cost, _, node = heapq.heappop(frontier)
        if visited[node.state.to_tuple()] < cost:
            continue
        if problem.goal_test(node.state):
            return node
        for child in node.expand(problem):
            if node.parent and child.state.to_tuple() == node.parent.state.to_tuple():
                continue
            child_tuple = child.state.to_tuple()
            if child_tuple not in visited or child.path_cost < visited[child_tuple]:
                visited[child_tuple] = child.path_cost
                heapq.heappush(frontier, (child.path_cost, unique_id, child))
                unique_id += 1
    return None