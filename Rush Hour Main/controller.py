import os
from solver import RushHourSolver

class RushHourController:
    def __init__(self):
        self.solver = RushHourSolver()

    def get_available_maps(self):
        return [f for f in os.listdir("maps") if f.endswith(".txt")]

    def play(self, map_name, algo):
        self.solver.load_map(f"maps/{map_name}")
        self.solver.set_algorithm(algo)
        self.solver.solve()

    def pause(self):
        pass

    def reset(self):
        pass