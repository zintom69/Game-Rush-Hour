from collections import deque


def bfs_search(start):
    queue = deque()
    visited = set()
    queue.append((start, []))
    visited.add(start.to_tuple())

    while queue:
        state, path = queue.popleft()
        if state.isGoal():
            return path
        for k in state.vehicles:
            for move_val in [-1, 1]:
                new_state = state.copy()
                if new_state.move(k, move_val):
                    t = new_state.to_tuple()
                    if t not in visited:
                        visited.add(t)
                        queue.append((new_state, path + [(k, move_val)]))
    return None