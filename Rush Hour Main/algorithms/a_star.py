import heapq
from .search import Node

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def append(self, item, priority):
        heapq.heappush(self.heap, (priority, self.count, item))
        self.count += 1

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[-1]
        raise Exception('Error: Empty queue')

    def __len__(self):
        return len(self.heap)

def a_star_search(problem):
    node = Node(problem.initial_state)
    frontier = PriorityQueue()
    frontier.append(node, node.path_cost + problem.h(node.state))
    explored = dict()  # instead of set in AIMA

    while frontier:
        current_node = frontier.pop()
        if problem.goal_test(current_node.state):
            # if display:
            #     print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return current_node
        state_tuple = current_node.state.to_tuple()
        if state_tuple in explored and explored[state_tuple] <= current_node.path_cost:
            continue
        explored[state_tuple] = current_node.path_cost
        for child in current_node.expand(problem):
            child_tuple = child.state.to_tuple()
            f = child.path_cost + problem.h(child.state)
            if child_tuple not in explored or child.path_cost < explored[child_tuple]:
                frontier.append(child, f)
    return None