from vehicle import Vehicle

class Board:
    def __init__(self, rows=6, cols=6): 
        self.rows= rows         
        self.cols = cols
        self.grid = []
        self.makeGrid(self.rows + 1)
        # self.level = 0
        self.vehicles = {} # list chứa car -> lưu dạng dict: [kind] - [index, pos, len, dir]
        self.stages = [] # state

        
    # Read file -> map
    def readMap(self, map_index):
        map_path = "./maps/map" + str(map_index + 1) + ".txt"
        with open(map_path, "r") as map_file:
            for line in map_file:
                word = line.strip().split()
                block = []
                for letter in word:
                    if letter.isdigit():
                        block.append(int(letter))
                    else:
                        block.append(letter)
                self.stages.append(block)
    
    # Draw map in text
    def __str__(self):
        ret_str = "\n"
        for i in range(self.rows):
            for j in range(self.cols):
                ret_str += str(self.grid[j][i])
                ret_str += " "
            ret_str += "\n"
        ret_str += "\n"
        return ret_str


    def makeGrid(self, size):
        for i in range(size):
            self.grid.append(["*"]*size)
    
    def clearGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = "*"

    # 
    def stagePrepare(self):
        self.clearGrid()
        self.vehicles = {}
        # curr_lev_stage = self.stages[self.level]
        curr_stage = self.stages
        for v in curr_stage:
            self.pushVehicle(Vehicle(v[0], [v[1], v[2]], v[3], v[4]))
    
    def pushVehicle(self, vehicle):
        vPos = vehicle.pos
        vLen = vehicle.len
        vDir = vehicle.dir
        vKind = str(vehicle.index)

        isUpdated = True

        if vKind in self.vehicles:
            return False
        # print(vPos)
        if vDir == 'h':
            if vPos[0] < 0 and vPos[0] > self.cols - 1 - vLen and \
                vPos[1] < 0 and vPos[1] > self.rows - 1:
                return False

            for i in range(vPos[0], vPos[0] + vLen):
                if self.grid[i][vPos[1]] != "*":
                    isUpdated = False
                    return False

            if isUpdated:
                self.vehicles[vKind] = vehicle
                for i in range(vPos[0], vPos[0] + vLen):
                    self.grid[i][vPos[1]] = vKind
                return True

        elif vDir == 'v':
            if vPos[0] < 0 and vPos[0] > self.cols - 1 and \
                vPos[1] < 0 and vPos[1] > self.rows - 1 - vLen :
                return False

            for i in range(vPos[1], vPos[1] + vLen):
                if self.grid[vPos[0]][i] != "*":
                    isUpdated = False
                    return False

            if isUpdated:
                self.vehicles[vKind] = vehicle
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grid[vPos[0]][i] = vKind
                return True

        
    def isOnboard(self, kind):
        if kind not in self.vehicles:
            return False
        else:
            return True

    # Move function -> with val
    def move(self, kind, val):

        if kind not in self.vehicles:
            return False

        vehicle = self.vehicles[kind]
        vPos = vehicle.pos
        vLen = vehicle.len
        vDir = vehicle.dir
        vKind = str(vehicle.index)

        isUpdated = True

        if kind == '0' and vPos[0] ==  4:
            self.vehicles['0'].pos = (6,2)
            return True


        if vDir == 'h':
            if vPos[0] + val < 0 or vPos[0] + val > self.cols - vLen or \
                vPos[1]  < 0 or vPos[1] > self.rows - 1:
                return False

            for i in range(vPos[0] + val, vPos[0]+val + vLen):
                if self.grid[i][vPos[1]] != "*":
                    if self.grid[i][vPos[1]] != vKind:
                        isUpdated = False
                        return False

            if isUpdated:
                # Assign "*" old place
                for i in range(vPos[0], vPos[0] + vLen):
                    self.grid[i][vPos[1]] = "*"
                
                self.vehicles[vKind].pos[0] += val
                vPos = vehicle.pos

                for i in range(vPos[0], vPos[0] + vLen):
                    self.grid[i][vPos[1]] = vKind
                return True

        elif vDir == 'v':
            if vPos[0] < 0 or vPos[0] > self.cols - 1 or \
                vPos[1] + val < 0 or vPos[1] + val > self.rows - vLen :
                return False

            for i in range(vPos[1] + val, vPos[1] + val + vLen):
                if self.grid[vPos[0]][i] != "*":
                    if self.grid[vPos[0]][i] != vKind:
                        isUpdated = False
                        return False

            if isUpdated:
                # Assign "*" old place
                for j in range(vPos[1], vPos[1] + vLen):
                    self.grid[vPos[0]][j] = "*"
        
                self.vehicles[vKind].pos[1] += val
                vPos = vehicle.pos
                self.grid[vPos[0]][vPos[1] - val] = "*"
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grid[vPos[0]][i] = vKind
                return True
    
    def is_move(self, kind, val):
        if kind not in self.vehicles:
            return False

        vehicle = self.vehicles[kind]
        vPos = vehicle.pos
        vLen = vehicle.len
        vDir = vehicle.dir
        vKind = str(vehicle.index)

        if kind == '0' and vPos[0] == 4:
            return True

        if vDir == 'h':
            new_x = vPos[0] + val

            
            if new_x < 0 or new_x > self.cols - vLen or vPos[1] < 0 or vPos[1] >= self.rows:
                return False
            if val > 0: 
                for i in range(vPos[0], new_x + vLen):
                    if self.grid[i][vPos[1]] != "*" and self.grid[i][vPos[1]] != vKind:
                        return False
            else:
                for i in range(new_x, vPos[0]):
                    if self.grid[i][vPos[1]] != "*" and self.grid[i][vPos[1]] != vKind:
                        return False
            return True

        elif vDir == 'v':
            new_y = vPos[1] + val
            if vPos[0] < 0 or vPos[0] >= self.cols or new_y < 0 or new_y > self.rows - vLen:
                return False
            if val > 0: 
                for i in range(vPos[1], new_y + vLen):
                    if self.grid[vPos[0]][i] != "*" and self.grid[vPos[0]][i] != vKind:
                        return False
            else: 
                for i in range(new_y, vPos[1]):
                    if self.grid[vPos[0]][i] != "*" and self.grid[vPos[0]][i] != vKind:
                        return False
            return True

        return False

    
    def isGoal(self):
        vehicle_x = self.vehicles['0']
        if vehicle_x.pos[0] >= 4 and vehicle_x.pos[1] == 2:
            return True
        else:
            return False
    
    def copy(self):
        new_board = Board(self.rows, self.cols)

        new_board.grid = []
        for row in self.grid:
            new_board.grid.append(row[:])  

        new_board.stages = []
        for stage in self.stages:
            new_board.stages.append(stage[:]) 
        
        new_board.vehicles = {}
        for vehicle_id, vehicle in self.vehicles.items():
            new_vehicle = Vehicle(
                vehicle.index,
                [vehicle.pos[0], vehicle.pos[1]],
                vehicle.len,
                vehicle.dir
            )
            new_board.vehicles[vehicle_id] = new_vehicle
        
        return new_board
    def to_tuple(self):
        grid_tuple = tuple(tuple(row) for row in self.grid)
  
        vehicles_tuple = tuple(
            (vehicle_id, tuple(vehicle.pos)) 
            for vehicle_id, vehicle in sorted(self.vehicles.items())
        )
        
        return (grid_tuple, vehicles_tuple)
    
    def compare(self, other_board):
        if not isinstance(other_board, Board):
            return False
        return self.to_tuple() == other_board.to_tuple()