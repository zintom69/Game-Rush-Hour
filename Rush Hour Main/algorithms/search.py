# from ..algorithms import bfs, dfs, ucs, a_star
TIME_LIMIT = 600
import time

class Problem:
    def __init__(self, initial_state, goal=None):
        self.initial_state = initial_state
        self.goal = goal
    
    
    def actions(self, state):
        actions = []
        for vehicle in state.vehicles:
            for step in range(-4, 5):
                if step != 0 and state.is_move(vehicle, step):
                    actions.append((vehicle, step))
        return actions
    
    def result(self, state, action):
        new_state = state.copy()
        kind, step = action
        new_state.move(kind, step)
        return new_state
    
    def goal_test(self, state):
        return state.isGoal()
        
    # Path cost = number of move step of car
    def path_cost(self, c, state1, action, state2):
        kind, step = action
        vehicle_length = state1.vehicles[kind].len
        if (state2.compare(self.result(state1, action))):
            return c + abs(step)
        else:
            raise Exception("is not in the valid state")
    
    def h(self, state):
        # Heuristic nâng cao: Đếm số xe chắn phía trước xe đỏ và số xe chặn các xe chắn đó
        red_car = state.vehicles.get('0')
        if not red_car:
            return 0
        row = red_car.pos[1]
        col = red_car.pos[0] + red_car.len
        count = 0
        extra_moves = 0
        checked_blocks = set()
        for c in range(col, state.cols):
            cell = state.grid[c][row]
            if cell != '*' and cell != '0' and cell not in checked_blocks:
                count += 1
                checked_blocks.add(cell)
                block_vehicle = state.vehicles.get(cell)
                # Nếu là xe dọc, kiểm tra có bị xe khác chặn trên/dưới không
                if block_vehicle and block_vehicle.dir == 'v':
                    # Kiểm tra phía trên
                    for up in range(row-1, -1, -1):
                        up_cell = state.grid[c][up]
                        if up_cell != '*' and up_cell != cell:
                            extra_moves += 1
                            break
                    # Kiểm tra phía dưới
                    for down in range(row+1, state.rows):
                        down_cell = state.grid[c][down]
                        if down_cell != '*' and down_cell != cell:
                            extra_moves += 1
                            break
        return count + extra_moves


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.state.to_tuple() == other.state.to_tuple()

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def get_depth(self):
        return self.depth