from collections import deque
from algorithms.base import SearchAlgorithm

class BFS(SearchAlgorithm):
    def solve(self, puzzle):
        start_state = puzzle
        queue = deque([start_state])
        visited = set()
        parent = {start_state: None}

        while queue:
            current = queue.popleft()
            if current.is_goal():
                return self.reconstruct_path(parent, current)

            visited.add(current)

            for neighbor in current.get_successors():
                if neighbor not in visited and neighbor not in queue:
                    parent[neighbor] = current
                    queue.append(neighbor)

        return []

    def reconstruct_path(self, parent, state):
        path = []
        while state:
            path.append(state)
            state = parent[state]
        return path[::-1]
