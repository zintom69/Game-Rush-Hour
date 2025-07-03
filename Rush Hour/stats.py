import time, psutil, os, csv

class Statistics:
    def start(self):
        self.time_start = time.perf_counter()
        self.process = psutil.Process(os.getpid())
        self.nodes_expanded = 0

    def end(self):
        self.time_end = time.perf_counter()
        self.memory_used = self.process.memory_info().rss / 1024 / 1024

    def increment_nodes(self):
        self.nodes_expanded += 1

    def save_to_csv(self, filename="stats.csv"):
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.time_end - self.time_start, self.memory_used, self.nodes_expanded])

