from vehicle import *

class Board:
    def __init__(self, rows=6, cols=6):
        self.rows= rows         
        self.cols = cols
        self.grid = []
        self.makeGrid(self.rows + 1)
        # self.level = 0
        self.vehicles = {} # list chứa car -> lưu dạng dict
        self.stages = [] # state

        
    # Read file -> map
    def readMap(self, map_index):
        map_path = "./maps/map" + str(map_index) + ".txt"
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
                if val > 0:
                    self.grid[vPos[0]][vPos[1]] = 0
                else:
                    self.grid[vPos[0] + vLen - 1][vPos[1]]=0
                self.vehicles[vKind].pos[0] += val
                vPos = vehicle.pos

                for i in range(vPos[0], vPos[0] + vLen):
                    self.grid[i][vPos[1]] = vKind
                return True

        

        elif vDir == 'v':
            if vPos[0] < 0 or vPos[0] > self.cols - 1 or \
                vPos[1] + val < 0 or vPos[1] + val > self.rows - vLen :
                return False

            for i in range(vPos[1] +val, vPos[1]+val + vLen):
                if self.grid[vPos[0]][i] != "*":
                    if self.grid[vPos[0]][i] != vKind:
                        isUpdated = False
                        return False

            if isUpdated:
                if val > 0:
                    self.grid[vPos[0]][vPos[1]] = "*"
                else:
                    self.grid[vPos[0]][vPos[1]+vLen - 1]=0
                self.vehicles[vKind].pos[1] += val
                vPos = vehicle.pos
                self.grid[vPos[0]][vPos[1] - val] = 0
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grid[vPos[0]][i] = vKind
                return True
    def isGoal(self):
        vehicle_x = self.vehicles['0']
        if vehicle_x.pos[0] >= 4 and vehicle_x.pos[1] == 2:
            # self.vehicles['x'].pos = (6,2)
            return True
        else:
            return False
    
    