from collections import deque
from .search import Problem, Node, time, TIME_LIMIT

def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial_state)])  
    visited = set()
    visited.add(problem.initial_state.to_tuple())
    start_time = time.time()

    while frontier:
        if time.time() - start_time > TIME_LIMIT:
            print("Time limit exceeded!")
            return None
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        for child in node.expand(problem):
            child_tuple = child.state.to_tuple()
            if child_tuple not in visited:
                visited.add(child_tuple)
                frontier.append(child)
    return None

