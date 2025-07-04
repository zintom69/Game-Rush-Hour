from puzzle import RushHourPuzzle
from stats import Statistics
from algorithms import bfs #, dfs, ucs, astar

class RushHourSolver:
    def __init__(self):
        self.algorithm = None
        self.puzzle = None
        self.stats = Statistics()

    def load_map(self, path):
        self.puzzle = RushHourPuzzle.from_file(path)

    def set_algorithm(self, name):
        if name == "BFS":
            self.algorithm = bfs.BFS()
        # elif name == "DFS":
        #     self.algorithm = dfs.DFS()
        # elif name == "UCS":
        #     self.algorithm = ucs.UCS()
        # elif name == "A*":
        #     self.algorithm = astar.AStar()

    def solve(self):
        self.stats.start()
        solution = self.algorithm.solve(self.puzzle)
        self.stats.end()
        self.stats.save_to_csv()

