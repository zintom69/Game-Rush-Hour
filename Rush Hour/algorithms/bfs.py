from collections import deque

def bfs_search(board):
    """
    BFS algorithm adapted for the Rush Hour puzzle
    """
    # Check if already at goal state
    if board.isGoal():
        return []
    
    # Initialize queue with starting state and empty moves list
    queue = deque([(board, [])])
    visited = set([board.to_tuple()])
    
    while queue:
        current_board, moves = queue.popleft()
        
        # Get all possible moves for current board state
        possible_moves = get_possible_moves(current_board)
        
        for vehicle_id, steps in possible_moves:
            # Create a copy of the current board
            new_board = current_board.copy()
            
            # Make the move
            if new_board.move(vehicle_id, steps):
                # Get the new state
                state = new_board.to_tuple()
                
                # Check if we've visited this state before
                if state not in visited:
                    visited.add(state)
                    new_moves = moves + [(vehicle_id, steps)]
                    
                    # Check if we reached the goal
                    if new_board.isGoal():
                        return new_moves
                    
                    # Add to queue for further exploration
                    queue.append((new_board, new_moves))
    
    # No solution found
    return None

def get_possible_moves(board):
    """
    Generate all possible moves for the current board state
    """
    possible_moves = []
    
    # Iterate through all vehicles on the board
    for vehicle_id in board.vehicles:
        vehicle = board.vehicles[vehicle_id]
        
        if vehicle.dir == 'h':  # Horizontal vehicle
            # Try moving left (negative steps)
            for steps in range(-1, -(board.cols - vehicle.pos[0]), -1):
                if can_move(board, vehicle_id, steps):
                    possible_moves.append((vehicle_id, steps))
                else:
                    break
            
            # Try moving right (positive steps)
            for steps in range(1, board.cols - vehicle.pos[0] - vehicle.len + 1):
                if can_move(board, vehicle_id, steps):
                    possible_moves.append((vehicle_id, steps))
                else:
                    break
                    
        elif vehicle.dir == 'v':  # Vertical vehicle
            # Try moving up (negative steps)
            for steps in range(-1, -(board.rows - vehicle.pos[1]), -1):
                if can_move(board, vehicle_id, steps):
                    possible_moves.append((vehicle_id, steps))
                else:
                    break
            
            # Try moving down (positive steps)
            for steps in range(1, board.rows - vehicle.pos[1] - vehicle.len + 1):
                if can_move(board, vehicle_id, steps):
                    possible_moves.append((vehicle_id, steps))
                else:
                    break
    
    return possible_moves

def can_move(board, vehicle_id, steps):
    """
    Check if a vehicle can move by the specified number of steps
    """
    if vehicle_id not in board.vehicles:
        return False
        
    vehicle = board.vehicles[vehicle_id]
    vPos = vehicle.pos
    vLen = vehicle.len
    vDir = vehicle.dir
    
    if vDir == 'h':  # Horizontal movement
        new_x = vPos[0] + steps
        # Check bounds
        if new_x < 0 or new_x + vLen > board.cols:
            return False
        
        # Check for collisions with other vehicles
        if steps > 0:  # Moving right
            for i in range(vPos[0] + vLen, new_x + vLen):
                if board.grid[i][vPos[1]] != 0:
                    return False
        else:  # Moving left
            for i in range(new_x, vPos[0]):
                if board.grid[i][vPos[1]] != 0:
                    return False
                    
    elif vDir == 'v':  # Vertical movement
        new_y = vPos[1] + steps
        # Check bounds
        if new_y < 0 or new_y + vLen > board.rows:
            return False
        
        # Check for collisions with other vehicles
        if steps > 0:  # Moving down
            for i in range(vPos[1] + vLen, new_y + vLen):
                if board.grid[vPos[0]][i] != 0:
                    return False
        else:  # Moving up
            for i in range(new_y, vPos[1]):
                if board.grid[vPos[0]][i] != 0:
                    return False
    
    return True

# BFS class for compatibility with solver.py
class BFS:
    def solve(self, puzzle):
        return bfs_search(puzzle)